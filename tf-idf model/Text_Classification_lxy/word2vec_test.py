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

def build_sentence_vector(text,size,imdb_w2v):
    vec=np.zeros(size).reshape(1, size)
    count=0
    for word in text:
        try:
            vec+=imdb_w2v.wv[word].reshape((1,size))
            count+=1
        except KeyError:
            continue
    if count !=0:
        vec/=count
    return vec

if __name__ == '__main__':
    data_path = "./data/train.csv"
    data, features, targets = read_data(data_path)
    X_train, X_test, y_train, y_test = divide_set(data, targets, 0.3)
    vector_size = 5000
    model = Word2Vec(vector_size=vector_size,
                     min_count=1,  # 词频阈值 词出现的频率 小于这个频率的词 将不予保存
                     window=5  # 窗口大小 表示当前词与预测词在一个句子中的最大距离是多少
                     )
    model.build_vocab(X_train)
    model.train(X_train, total_examples=model.corpus_count, epochs=50)
    train_vec = np.concatenate([build_sentence_vector(z, vector_size, model) for z in X_train])
    print(train_vec.shape)
    model.train(X_test, total_examples=model.corpus_count, epochs=50)
    test_vec = np.concatenate([build_sentence_vector(z, vector_size, model) for z in X_test])
    print(test_vec.shape)

    print('Start training')
    forest = RandomForestClassifier(n_estimators=100)
    forest = forest.fit(train_vec, y_train)
    joblib.dump(filename='model/forest_word2vec.model', value=forest)

    print('Start testing')
    score = evaluate(forest, test_vec, y_test)
    print('Score: ', score)






