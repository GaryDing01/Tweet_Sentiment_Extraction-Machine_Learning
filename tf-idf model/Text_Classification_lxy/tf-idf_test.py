"""
@Author: lxy-146
@Description: emotion classification of tweet data with tfidf and lr
@Filetype: tweet_classification.py
@Time: 2022/5/8:13:59
"""
# 70%
# PCA，IODA
import jieba
import re
import csv
import sys
import time
import sklearn
from sklearn.linear_model import LogisticRegression
from sklearn import svm, tree
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from random_forest import RandomForest
from sklearn.model_selection import GridSearchCV
from nltk.corpus import stopwords
import joblib
import pandas as pd
import numpy as np
from scipy import sparse
from tool import read_data, evaluate, divide_set

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
    feature_name = vectorizer.get_feature_names()
    return X_train_tfidf, X_test_tfidf, vectorizer, feature_name

def main():
    # step1 读取数据（文本和停用词）
    data_path = "./data/train.csv"
    # data: text,selected_text,sentiment 27481
    data, features, targets = read_data(data_path)
    # step2 分词、分为训练集和测试集
    X_train, X_test, y_train, y_test = divide_set(data, targets, 0.3)

    # step3 提取特征参数（tf-idf）len(feature_name) == 21491
    X_train_tfidf, X_test_tfidf, tfidf_model, feature_name = calculate_tfidf(X_train, X_test)

    # Read: sparse.load_npz('file_path')
    # sparse.save_npz('feature/X_train_tfidf.npz', X_train_tfidf)
    # sparse.save_npz('feature/X_test_tfidf.npz', X_test_tfidf)

    # step4 训练模型
    # 99.82 41.99
    # clf = LogisticRegression(penalty='l2')

    # clf = RandomForestClassifier(n_estimators=100)
    clf = RandomForest(tree_num=100)
    # 99.82 41.99
    # clf = tree.DecisionTreeClassifier()
    # clf = svm.SVC()

    clf.fit(X_train_tfidf, y_train)
    # step5 模型评估
    accuracy = evaluate(clf, X_train_tfidf, y_train)
    print("训练集正确率：%.4f%%\n" % (accuracy * 100))

    accuracy = evaluate(clf, X_test_tfidf, y_test)
    print("测试集正确率：%.4f%%\n" % (accuracy * 100))

if __name__ == "__main__":
    start = time.clock()

    main()
    # lxy_random_forest()

    end = time.clock()
    print('execute time: ', (end - start))
