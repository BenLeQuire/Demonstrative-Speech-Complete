from flask import Flask, render_template, request
from waitress import serve
import cryptography
import json
from dotenv import load_dotenv
import os


db_url = os.getenv("DB_URL")
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')
@app.route('/callApp', methods=['POST'])
def callApp():
    answer_data = request.get_json()
    output = answer_data.get('output', 'no output found')
    return output



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    #serve(app, host='0.0.0.0', port=8000, threads = 8)