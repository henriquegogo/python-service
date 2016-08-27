import requests, json, re
from pyquery import PyQuery
from flask import Flask
app = Flask(__name__, static_url_path='')

@app.route("/")
def index():
    return app.send_static_file('index.html')

@app.route("/update/<symbol>")
def update(symbol=None):
    return "Updating {}".format(symbol)

@app.route("/statistics/<symbol>")
def statistics(symbol):
    url = "http://www.reuters.com/finance/stocks/financialHighlights?symbol={}".format(symbol)
    response = requests.get(url)
    dom = PyQuery(response.text)
    info = {
        'title': dom('#sectionTitle h1').text(),
        'symbol': re.search('\((.*)\)', dom('#sectionTitle h1').text()).group(1),
        'price_to_earnings': dom('td:contains("P/E Ratio")').next().text(),
        'price_to_book': dom('td:contains("Price to Book")').next().text(),
        'dividend_yeld': dom('td:contains("Dividend Yield")').next().text().split(' ')[0],
        'current_ratio': dom('td:contains("Current Ratio")').next().text(),
        'avg_volume': dom('span:contains("Avg. Vol")').next().next().text().replace(',','')
    }
    return json.dumps(info)

if __name__ == "__main__":
    app.run()
