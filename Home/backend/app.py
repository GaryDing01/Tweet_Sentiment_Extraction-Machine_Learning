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
@app.route('/open', methods=['get'])
def get_info():
    # cp = configparser.ConfigParser()
    # cur_path = os.getcwd()
    # cp.read(cur_path + '/server/cc.cfg')
    # sections = cp.sections()
    response = {
        'code': 0,
        'data': {}
    }
    # if len(sections) == 0:
    #     raise Exception('文件不存在或无内容')
    # for section in sections:
    #     response['data'][section] = {}
    #     for key in cp[section]:
    #         response['data'][section][key] = cp.get(section, key)

    return json.dumps(response, ensure_ascii=False)

@app.route('/get_result', methods=['GET', 'POST'])
def get_result():
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
@app.route('/open', methods=['post'])
def set_info():
    req = json.loads(request.data)

    response = {
        'code': 0,
        'data': req
    }
    return json.dumps(response)


if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    app.run()

