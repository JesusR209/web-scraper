from bs4 import BeautifulSoup
import requests
from flask import Flask, render_template


# WEB SCRAPER 

website = "https://www.scrapethissite.com/pages/"
result = requests.get(website)
html_data = result.text

soup = BeautifulSoup(html_data, "lxml")
links = soup.find_all(class_= "page-title")

# Prints link text in terminal

for link in links:
    print("THIS IS A CARD\n",link.text)



    # FLASK APP
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', links = links)

if __name__ == '__main__':
    app.run(debug=True)

    

    
    # use jinja and flask to create new cards.
    # once that is done push the repo to github :)
    # this is your first actual scraper pat yourself on the back!
    
    