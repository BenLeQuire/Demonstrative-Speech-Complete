from flask import Flask, render_template
from waitress import serve
import cryptography
import OpenSSL

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    #app.run()
    serve(app, host='1.1.1.1', port=8000, threads = 8)