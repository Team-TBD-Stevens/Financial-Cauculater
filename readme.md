
## FE 595 Midterm

\
\
**Purpose**
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
A collaborative project between group members Yuwen Jin, Minghao Kang, Fangchi Wu, and Shiraz Bheda. Our purpose was to create a website with multiple features for options pricing, including user input, data visualization, and a comparison of runtime metrics that varies with source of historical data. The idea of this tool is that it will serve as a baseline for a potentially marketable product for end users who want to price out options quickly using their own assumptions in a clean and presentable web interface.
\
\
**Inspiration**
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
We wanted to apply some of the skills we have learned in this class towards created fast and user-friendly financial tools. One of the main benefits of this project is that it has a lot of built-in user flexibility that allows for detailed results with a faster turnaround time than any simple solver-driven excel sheet can provide. Importantly, this project represents a baseline that is very scalable if the data is stored in a database, as opposed to downloading the necessary historical data from a package with every user request. Observing the differences in runtime helped in forming this conclusion and developing a product that is much more scalable.

**List of Functions**
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
1. We were partly inspired by the challenge of applying the skills we have learned in this class in a financial setting.
2. Language Detect: returns the name of the most possible language that the string is written in
3. Tokenize: tokenizes the string
4. Top Ten: returns a list of up to ten of the most frequently used words
5. Part of Speech Tagging: assigns each word in the string to a part of speech
6. English to French: translates the string from English to French
7. English to Chinese: translates the string from English to Chinese
8. Spell Check: returns spell check result of the text

\
\
**Instructions**
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
One way to **access the website** is to run 'flask api.py' in this project directly. In this case, if you're using Windows system the homepage address is '127.0.0.1:5000', and if you're using ios system the address is '0.0.0.0:8000'. 
The other way is to launch your AWS instance and connect to your running instance via your terminal. After installing git and python3, and using git clone to clone the repository to your terminal,you will need to install the requirements of the flask api prior to running the script itself.

**Open the home page**, enter text in the blank text box and select method(s) via check box, click 'submit' button then you'll see the result page. 
If the text entry is blank you'll receive a message saying 'your text is empty', while if you click 'submit' without choosing any analyzing method you'll get another message saying 'please choose at least one analyzing method'. The 'back' button can take you back to the previous page.

NOTE: While most of the required packages to run this script have been placed on a 'requirements.txt' page, there is a subfolder titled 'materials' that contains several additional packages that may need to be manually installed by accessing the file path directory. Once this has been completed, you can uncomment lines in 'flask api.py', 'home.html' and 'result.html', then you'll see another NLP toy, an AI response machine.

\
\
**Example output**
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
[![Screenshot-2020-11-09-213940.png](https://i.postimg.cc/1XKdF8fZ/Screenshot-2020-11-09-213940.png)](https://postimg.cc/sGvKdDYn)

