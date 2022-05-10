import requests
from flask import Flask
from tkinter import *
from bs4 import BeautifulSoup


# app = Flask(__name__)

# @app.route("/")
# def hello_world():

URL ="https://www.microcenter.com/search/search_results.aspx?N=&cat=&Ntt=3090&searchButton=search"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="pricing")

for num in soup.find_all('a',{"data-category":"Graphics Cards"}):
    print(num.text.strip())

for price in soup.find_all('span', {"itemprop":"price"}):
    print(price.text.strip())


# root = Tk()
# myLabel = Label(root, text=card_price.text.strip())
# root.geometry("900x500")
# myLabel.pack()
# root.mainloop()


