"""
@Author: lxy-146
@Description: 
@Filetype: neutral_network.py
@Time: 2022/6/5:8:31
"""
from sklearn.neural_network import MLPClassifier
from tool import read_data, evaluate, divide_set
from sklearn.feature_extraction.text import CountVectorizer
import time

def main():
    data_path = "./data/train.csv"
    data, features, targets = read_data(data_path)
    vectorizer = CountVectorizer(analyzer='word', tokenizer=None, preprocessor=None, stop_words=None, max_features=5000)

    X_train, X_test, y_train, y_test = divide_set(data, targets, 0.3)
    train_feature = vectorizer.fit_transform(X_train)
    test_feature = vectorizer.transform(X_test)

#     设置分类器 solver={‘lbfgs’, ‘sgd’, ‘adam’} activation={'relu','logistic'}
    clf = MLPClassifier(solver='lbfgs', activation='relu', hidden_layer_sizes=(100, 100), max_iter=400)  # 使用反向传播和sigmoid激活
    print('layer')
    print('Start fit!')
    clf.fit(train_feature, y_train)
    print('Start test!')
    print('Train Score: ', clf.score(train_feature, y_train))
    print('Test Score: ', clf.score(test_feature, y_test))

if __name__ == '__main__':
    start = time.clock()

    main()

    end = time.clock()
    print('execute time: ', (end - start))