from flask import Flask, render_template
from waitress import serve
import cryptography
import OpenSSL
import werkzeug

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
    #serve(app, host='0.0.0.0', port=8000, threads = 8)