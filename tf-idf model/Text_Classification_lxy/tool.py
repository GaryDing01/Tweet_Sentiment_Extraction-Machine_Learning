"""
@Author: lxy-146
@Description: 
@Filetype: tool.py
@Time: 2022/5/22:10:44
"""
import re
import csv
import sklearn
from bs4 import BeautifulSoup
from nltk.corpus import stopwords


def read_data(data_path):
    """
    读取数据
    :param data_path: 数据存放路径
    :return: 读取到的数据
    """
    StopWords = stopwords.words("english")
    data = []
    features = []
    targets = []
    with open(data_path, 'r') as f:
        reader = csv.reader(f)
        for item in reader:
            if reader.line_num == 1:
                continue
            # text = BeautifulSoup(item[1]).get_text()
            text = item[1].lower()
            text = re.sub('[^A-Za-z]+', ' ', text)
            data.append(''.join([word + ' ' for word in text.split() if word not in StopWords]))
            features.append(item[2])
            targets.append(item[3])
            # if item[3] == 'neutral':
            #     targets.append(0)
            # elif item[3] == 'positive':
            #     targets.append(1)
            # else:
            #     targets.append(2)
    return data, features, targets

def divide_set(data, targets, test_size):
    """
    进行将训练集和测试集分开
    :param data:
    :param target:
    :return:
    """
    X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(data, targets, test_size=test_size, random_state=1028)
    return X_train, X_test, y_train, y_test

def evaluate(model, X, y):
    """
    模型评估
    :param model: 训练好的模型
    :param X: 测试集
    :param y: 测试集标签
    :return: 正确率和auc值
    """
    accuracy = model.score(X, y)
    # fpr, tpr, thresholds = sklearn.metrics.roc_curve(y, model.predict_proba(X)[:, 1], pos_label=1)
    return accuracy