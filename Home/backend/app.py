"""
@Author: lxy-146
@Description: 
@Filetype: app.py.py
@Time: 2022/6/17:11:17
"""
from flask import Flask, json, request, jsonify
from flask_cors import CORS
import json
import configparser
import os
from tool import *
from models import Model

# configuration
DEBUG = True

# instance the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resource={r'/*': {'origins': '*'}})

# sanity check route

@app.route('/get_result_tfidf_l', methods=['GET', 'POST'])
def get_result1():
    file = request.files.get('file')
    filename = file.filename
    file_path = os.path.join('data', filename)
    file.save(file_path)
    data = get_data_from_csv(file_path)
    model = Model('tfidf', 'LogisticRegression')
    result = model.get_result(data)
    print(result)
    response = {
        "result": result
    }
    # return json.dumps(response, ensure_ascii=False)
    return jsonify(response)

@app.route('/get_result_tfidf_r', methods=['GET', 'POST'])
def get_result2():
    file = request.files.get('file')
    filename = file.filename
    file_path = os.path.join('data', filename)
    file.save(file_path)
    data = get_data_from_csv(file_path)
    model = Model('tfidf', 'RandomForestClassifier')
    result = model.get_result(data)
    print(result)
    response = {
        "result": result
    }
    # return json.dumps(response, ensure_ascii=False)
    return jsonify(response)

@app.route('/get_result_count_l', methods=['GET', 'POST'])
def get_result3():
    file = request.files.get('file')
    filename = file.filename
    file_path = os.path.join('data', filename)
    file.save(file_path)
    data = get_data_from_csv(file_path)
    model = Model('count', 'LogisticRegression')
    result = model.get_result(data)
    print(result)
    response = {
        "result": result
    }
    # return json.dumps(response, ensure_ascii=False)
    return jsonify(response)

@app.route('/get_result_count_r', methods=['GET', 'POST'])
def get_result4():
    file = request.files.get('file')
    filename = file.filename
    file_path = os.path.join('data', filename)
    file.save(file_path)
    data = get_data_from_csv(file_path)
    model = Model('count', 'RandomForestClassifier')
    result = model.get_result(data)
    print(result)
    response = {
        "result": result
    }
    # return json.dumps(response, ensure_ascii=False)
    return jsonify(response)

if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    app.run()

