"""
@Author: lxy-146
@Description: emotion classification of tweet data with tfidf and lr
@Filetype: tweet_classification.py
@Time: 2022/5/8:13:59
"""
import jieba
import re
import csv
import sys
import sklearn
from sklearn.linear_model import LogisticRegression
from sklearn import svm, tree
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import GridSearchCV
from nltk.corpus import stopwords
import joblib
import pandas as pd

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
            text = re.sub('[^A-Za-z]+', ' ', item[1])
            data.append(''.join([word+'' '' for word in text.split() if word not in StopWords]))
            features.append(item[2])
            targets.append(item[3])
            # if item[3] == 'neutral':
            #     targets.append(0)
            # elif item[3] == 'positive':
            #     targets.append(1)
            # else:
            #     targets.append(2)
    return data, features, targets

def calculate_tfidf(X_train, X_test):
    """
    计算文本的tf-idf
    :param X_train: 训练集
    :param X_test: 测试集
    :return: 返回的是文本的tf-idf特征
    """
    vectorizer = TfidfVectorizer()
    vectorizer.fit_transform(X_train)
    # joblib.dump(filename="model/vectorizer.model", value=vectorizer)
    # X_train_tfidf就是测试数据的特征矩阵
    X_train_tfidf = vectorizer.transform(X_train)
    X_test_tfidf = vectorizer.transform(X_test)
    # print(X_test_tfidf.toarray())
    feature_name = vectorizer.get_feature_names()
    # print(len(X_test), X_test_tfidf.shape)
    return X_train_tfidf, X_test_tfidf, vectorizer, feature_name

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

if __name__ == "__main__":
    # step1 读取数据（文本和停用词）
    data_path = "./data/train.csv"
    # data: text,selected_text,sentiment 27481
    data, features, targets = read_data(data_path)
    # print(targets)

    # step2 分词、分为训练集和测试集
    test_size = 0.1
    X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(data, targets, test_size=test_size, random_state=1028)

    # step3 提取特征参数（tf-idf）len(feature_name) == 21491
    X_train_tfidf, X_test_tfidf, tfidf_model, feature_name = calculate_tfidf(X_train, X_test)

    # step4 训练模型

    penaltys = ['l1', 'l2']
    Cs = [0.1, 1, 10, 100, 1000]
    # 调优的参数集合，搜索网格为2x5，在网格上的交叉点进行搜索
    tuned_parameters = dict(penalty=penaltys, C=Cs)


    # 99.82 41.99
    clf = LogisticRegression(solver='liblinear', C=10, penalty='l2')

    # 99.82 41.99
    # clf = tree.DecisionTreeClassifier()
    # clf = svm.SVC()

    clf.fit(X_train_tfidf, y_train)
    # step5 模型评估
    accuracy = evaluate(clf, X_train_tfidf, y_train)
    print("训练集正确率：%.4f%%\n" % (accuracy * 100))

    accuracy = evaluate(clf, X_test_tfidf, y_test)
    print("测试集正确率：%.4f%%\n" % (accuracy * 100))
