import sys
sys.path.append('lib')

from flask import Flask, request
app = Flask(__name__, static_url_path='')

@app.route("/")
def index():
    return app.send_static_file('index.html')

@app.route("/update/<symbol>")
def update(symbol=None):
    return "Updating %s" % symbol

@app.route("/statistics/<symbol>")
def statistics(symbol):
    return "Hello %s!" % symbol

if __name__ == "__main__":
    app.run()
