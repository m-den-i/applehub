# Copyright 2015 IBM Corp. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import random

from flask import Flask, jsonify, render_template, request, redirect

from cloudant.result import Result, ResultByKey
from cloudant.client import Cloudant
from alchemyapi_python.alchemyapi import AlchemyAPI
alchemyapi = AlchemyAPI()

app = Flask(__name__)
PORT_NUMBER = 8080
cred = {
  "username": os.environ['CLOUDANT_HOST'] + "-bluemix",
  "password": os.environ['CLOUDANT_PASSWORD'],
  "host": os.environ['CLOUDANT_HOST'] + "-bluemix.cloudant.com",
  "port": 443,
  "url": "https://" + os.environ['CLOUDANT_HOST'] + "-bluemix.cloudant.com"
}
client = Cloudant(cred['username'], cred['password'], url=cred['url'], account=cred['username'])
client.connect()
my_database = client['mydb']


@app.route('/joke')
def Welcome():
    all_docs = [doc for doc in my_database]
    return render_template('index.html', joke=random.choice(all_docs)['joke'])


@app.route('/')
def index():
    return render_template('main.html')


@app.route('/text')
def text():
    return 'Welcome again to my app running on Bluemix!'


@app.route('/api/people')
def GetPeople():
    list = [
        {'name': 'John', 'age': 28},
        {'name': 'Bill', 'val': 26}
    ]
    return jsonify(results=list)


@app.route('/api/people/<name>')
def SayHello(name):
    message = {
        'message': 'Hello ' + name
    }
    return jsonify(results=message)

port = os.getenv('PORT', '5000')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(port))
