from flask import Flask, render_template, request
import json
from dotenv import load_dotenv
import os
from flask_pymongo import PyMongo

db_url = os.getenv("DB_URL")

app = Flask(__name__)
app.config['MONGO_URI'] = db_url
mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('base.html')
@app.route('/callApp', methods=['POST'])
def callApp():
    answer_data = request.get_json()
    output = answer_data.get('output', 'no output found')
    db_entry = mongo.output.output.insert_1(output)

    return db_entry



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)