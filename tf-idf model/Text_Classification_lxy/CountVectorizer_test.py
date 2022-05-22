"""
@Author: lxy-146
@Description: 
@Filetype: CountVectorizer_test.py
@Time: 2022/5/22:16:09
"""
from tool import read_data, evaluate, divide_set
import sklearn
import joblib
import sys
import numpy as np
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer
from gensim.models.word2vec import Word2Vec
from gensim.corpora.dictionary import Dictionary
# 69%
if __name__ == '__main__':
    data_path = "./data/train.csv"
    data, features, targets = read_data(data_path)
    X_train, X_test, y_train, y_test = divide_set(data, targets, 0.3)

    vectorizer = CountVectorizer(analyzer='word', tokenizer=None, preprocessor=None, stop_words=None, max_features=5000)
    train_feature = vectorizer.fit_transform(X_train)
    print(train_feature.shape)
    train_feature_array = train_feature.toarray()
    vocab = vectorizer.get_feature_names()
    print('Start training')
    forest = RandomForestClassifier(n_estimators=100)
    forest = forest.fit(train_feature_array, y_train)
    joblib.dump(filename='model/forest_count_vectorizer.model', value=forest)
    print('Start testing')
    test_feature = vectorizer.transform(X_test)
    score = evaluate(forest, test_feature, y_test)
    print('Score: ', score)