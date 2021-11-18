# Covid-Tracker Bot
# pip install requests
# pip install BeautifulSoup4
# pip install pandas
# pip install folium
# pip install flask
import requests
from bs4 import BeautifulSoup
import pandas
import folium
from flask import Flask, render_template

Map = folium.Map(location=[33.5555, -7.5777], zoom_start=15)
Map.save('templates/Map.html')

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('Map.html')


@app.route("/bot")
def hello_bot():
    return '<h1>Hello bot</h1>'


app.run()
