from flask import Flask, jsonify
from bs4 import BeautifulSoup
import requests

def get_currency(in_currency, out_currency):
    url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1'
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    rate = soup.find('span', class_='ccOutputRslt').get_text()
    rate = float(rate[:-4])
    return rate

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Currency Rate API is running!</h1> <p>Example URL: /api/v1/eur-usd</p>"

@app.route('/api/v1/<string:in_cur>-<string:out_cur>')
def api(in_cur, out_cur):
    rate = get_currency(in_cur.upper(), out_cur.upper())
    result_dict = {
        "input_currency": in_cur.upper(),
        "output_currency": out_cur.upper(),
        "rate": rate
    }
    return jsonify(result_dict)

app.run()
