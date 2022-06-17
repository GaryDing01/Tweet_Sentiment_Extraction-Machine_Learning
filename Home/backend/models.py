"""
@Author: lxy-146
@Description: 
@Filetype: model.py
@Time: 2022/6/17:14:07
"""
from tool import *
import joblib
import os

class Model(object):
    def __init__(self, vectorizer_model_name, clf_model_name):
        self.model_path = 'model/' + vectorizer_model_name + '_model'
        self.vectorizer_model = self.get_vectorizer_model(vectorizer_model_name)
        self.clf_model = self.get_clf_model(clf_model_name)

    def get_vectorizer_model(self, model_name):
        if model_name == 'count' or model_name == 'tfidf':
            model_path = 'model/' + model_name + '_model/vectorizer.model'
            return joblib.load(filename=model_path)
        else:
            print('Error: wrong vectorizer model name!')

    def get_clf_model(self, model_name):
        model_path = os.path.join(self.model_path, model_name + '.model')
        return joblib.load(filename=model_path)

    def get_result(self, data):
        data_vec = self.vectorizer_model.transform(data)
        result_array = self.clf_model.predict(data_vec)
        result = []
        for r in result_array:
            result.append(r)
        return result