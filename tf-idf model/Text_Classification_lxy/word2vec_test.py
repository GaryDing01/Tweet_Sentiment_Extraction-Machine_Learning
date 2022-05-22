"""
@Author: lxy-146
@Description: 
@Filetype: word2vec_test.py
@Time: 2022/5/22:10:47
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

if __name__ == '__main__':
    data_path = "./data/train.csv"
    data, features, targets = read_data(data_path)
    # print(data[0])
    # print(data[100])
    # sys.exit(0)
    X_train, X_test, y_train, y_test = divide_set(data, targets, 0.3)
    # model = Word2Vec(data,  # 上文处理过的全部语料
    #                  size=100,  # 词向量维度 默认100维
    #                  min_count=1,  # 词频阈值 词出现的频率 小于这个频率的词 将不予保存
    #                  window=5  # 窗口大小 表示当前词与预测词在一个句子中的最大距离是多少
    #                  )
    # model.save('./feature/f.model')  # 保存模型

    vectorizer = CountVectorizer(analyzer='word', tokenizer=None, preprocessor=None, stop_words=None, max_features=5000)
    train_feature = vectorizer.fit_transform(X_train)
    print(train_feature.shape)
    train_feature_array = train_feature.toarray()
    vocab = vectorizer.get_feature_names()
    print('Start training')
    forest = RandomForestClassifier(n_estimators=100)
    forest = forest.fit(train_feature_array, y_train)
    joblib.dump(filename='model/forest.model', value=forest)
    print('Start testing')
    test_feature = vectorizer.transform(X_test)
    score = evaluate(forest, test_feature, y_test)
    print('Score: ', score)



