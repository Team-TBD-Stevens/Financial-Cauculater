from flask import Flask, render_template, request, url_for, flash
import pandas as pd
import numpy as np
import os
import yfinance as yf
import itertools
from commonoption import *
import quandl
import matplotlib.pyplot as plt
import urllib
from io import BytesIO
import base64
from lxml import etree
from sklearn.datasets import load_iris


app = Flask(__name__)
# tickers = ['AAPL', 'GOOG', 'ATVI']
# prechash_data = yf.download('AAPL', start="2010-01-01", end="2020-12-01")
risk_free = quandl.get('FRED/DGS1').iloc[-1, 0]



@app.route('/')
def home():
    return render_template('home.html')


@app.route('/result', methods=['POST', 'GET'])
def user_rec():
    pricing_model = request.form.getlist('pricing_model')
    option_type = request.form.getlist('option_type')
    ticker, S, K, r, T = read_in()
    adj_close = yf.download(ticker, start="2019-12-01", end="2020-12-01")['Adj Close']

    result_df = pd.DataFrame(columns=['model', 'option type', 'Expected PRICE'])
    title, prices, model, o_type, BS_bool, BS_df, BS_html = [], [], [], [], False, None, None
    call = CommonOption(call_or_put=1, maturity=T/365, spot_price=S, sigma=float(np.std(adj_close)),
                        risk_free_rate=r, strike_price=K, dividends=0)
    put = CommonOption(call_or_put=0, maturity=T/365, spot_price=S, sigma=float(np.std(adj_close)),
                       risk_free_rate=r, strike_price=K, dividends=0)
    [print(i) for i in [S, K, r, T]]
    if 'BS model' in pricing_model:
        BS_bool = True
        model = ['BS model']*2
        o_type = ['European Option']*2
        pricing_model.remove('BS model')
        BS_df = pd.DataFrame(columns=['delta', 'gamma', 'vega', 'theta', 'rho'], index=['call', 'put'])
        BS_df.iloc[0, :] = call.B_S_call_para()[1:]
        BS_df.iloc[1, :] = call.B_S_put_para()[1:]
    combination = list(itertools.product(pricing_model, option_type))

    [model.append(i) for i in np.array([[i[0]]*2 for i in combination]).flatten()]
    [o_type.append(i) for i in np.array([[i[1]]*2 for i in combination]).flatten()]
    result_df['model'] = np.array(model).flatten()
    result_df['option type'] = np.array(o_type).flatten()

    for i in range(int(result_df.shape[0])):
        if i % 2 == 0:
            title.append(ticker + ' ' + str(T) + ' day(s) call')
            prices.append(fit_model(result_df['model'][i], result_df['option type'][i], call))
        else:
            title.append(ticker + ' ' + str(T) + ' day(s) put')
            prices.append(fit_model(result_df['model'][i], result_df['option type'][i], put))
    result_df.index = title
    result_df['Expected PRICE'] = prices

    return render_template('result.html', result=result_df, BS_bool=BS_bool, BS_df=BS_df)


def read_in():
    ticker = request.form['ticker']
    try:
        S = float(request.form['S'])
    except ValueError:
        S = -1
        print('Please enter a number')
    try:
        K = float(request.form['K'])
    except ValueError:
        K = -1
        print('Please enter a number')
    try:
        r = float(request.form['r'])
    except:
        r = risk_free
    try:
        T = float(request.form['T'])
    except ValueError:
        T = -1
        print('Please enter a number')
    return ticker, S, K, r, T


def run_time():
    S = request.form['S']
    K = request.form['K']
    r = request.form['r']
    T = request.form['T']
    return S, K, r, T


def fit_model(model, option_type, option: CommonOption):
    price = -1
    if model == 'BS model':
        price = option.B_S()
    if model == 'Binomial Tree' and option_type == 'European Option':
        price = option.binomial_tree_EU(3)[0]
    elif model == 'Binomial Tree' and option_type == 'American Option':
        price = option.binomial_tree_US(3)[0]
    if model == 'Trinomial Tree' and option_type == 'European Option':
        price = option.trinomial_tree_EU(3)[0]
    elif model == 'Trinomial Tree' and option_type == 'American Option':
        price = option.trinomial_tree_US(3)[0]
    return round(price, 4)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
