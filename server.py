from flask import Flask, render_template, request
import json
from dotenv import load_dotenv
import os
from flask_pymongo import PyMongo
load_dotenv()

db_url = os.getenv("DB_URL")
#print(db_url)

app = Flask(__name__)
app.config['MONGO_URI'] = db_url
mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('base.html')
@app.route('/callApp', methods=['POST'])
def callApp():
    answer_data = request.get_json()
    print(answer_data)
    db_entry = mongo.db.output.insert_one(answer_data)

    return {'inserted_id': str(db_entry.inserted_id)}



if __name__ == '__main__':
    app.run(host='0.0.0.0')