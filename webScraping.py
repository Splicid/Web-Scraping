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

for num in range(0,9):
    card_price = soup.find('a',{"id":"hypProductH2_" + str(num)})
    print(card_price.text.strip())


# root = Tk()
# myLabel = Label(root, text=card_price.text.strip())
# root.geometry("900x500")
# myLabel.pack()
# root.mainloop()


