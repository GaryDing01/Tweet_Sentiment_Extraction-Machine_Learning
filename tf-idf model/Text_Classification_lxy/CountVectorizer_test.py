"""
@Author: lxy-146
@Description: 
@Filetype: CountVectorizer_test.py
@Time: 2022/5/22:16:09
"""
from tool import read_data, evaluate, divide_set
import sklearn
import joblib
import time
import sys
import csv
import numpy as np
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer
from random_forest import RandomForest
from gensim.models.word2vec import Word2Vec
from gensim.corpora.dictionary import Dictionary
from sklearn.linear_model import LogisticRegression

def lxy_random_forest():
    data_path = "./data/train.csv"
    data, features, targets = read_data(data_path)
    vectorizer = CountVectorizer(analyzer='word', tokenizer=None, preprocessor=None, stop_words=None, max_features=5000)
    all_feature = vectorizer.fit_transform(data)
    all_feature = all_feature.toarray()
    X_train, X_test, y_train, y_test = divide_set(data, targets, 0.3)
    vectorizer = CountVectorizer(analyzer='word', tokenizer=None, preprocessor=None, stop_words=None, max_features=5000)

    X_small_train = X_train[:2000]
    y_small_train = y_train[:2000]
    train_small_feature = vectorizer.fit_transform(X_small_train)
    forest = RandomForest(50)
    forest.fit(train_small_feature, y_small_train)
    X_small_test = X_test[:500]
    y_small_test = y_test[:500]
    test_small_feature = vectorizer.transform(X_small_test)
    score = evaluate(forest, test_small_feature, y_small_test)
    print('score: ', score)

def main():
    data_path = "./data/train.csv"
    data, features, targets = read_data(data_path)
    vectorizer = CountVectorizer(analyzer='word', tokenizer=None, preprocessor=None, stop_words=None, max_features=5000)
    # all_feature = vectorizer.fit_transform(data)
    # all_feature = all_feature.toarray()
    # print(all_feature.shape)
    # with open('model/count_feature.csv', 'a') as f:
    #     write = csv.writer(f)
    #     write.writerows(all_feature)
    # sys.exit(0)
    X_train, X_test, y_train, y_test = divide_set(data, targets, 0.3)

    train_feature = vectorizer.fit_transform(X_train)
    print(train_feature.shape)
    train_feature_array = train_feature.toarray()
    vocab = vectorizer.get_feature_names()

    print('Start training')
    # clf = LogisticRegression(penalty='l2')
    # clf = RandomForest(tree_num=100)
    clf = svm.SVC()
    # forest = RandomForestClassifier(n_estimators=100)
    clf = clf.fit(train_feature, y_train)
    # joblib.dump(filename='model/forest_count_vectorizer.model', value=forest)
    print('Start testing')
    test_feature = vectorizer.transform(X_test)
    score = evaluate(clf, test_feature, y_test)
    print('Score: ', score)


if __name__ == '__main__':

    start = time.clock()

    # main()
    lxy_random_forest()

    end = time.clock()
    print('execute time: ', (end - start))