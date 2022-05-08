"""
@author: lxy-146
@filetype: main.py
@time: 2022/5/6:10:57
"""
import jieba
import sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib
import pandas as pd


def read_data(data_path):
    """
    读取数据
    :param data_path: 数据存放路径
    :return: 读取到的数据
    """
    with open(data_path, 'r', encoding='utf-8') as f:
        data = f.readlines()
    return data

def get_stop_words(path):
    stopwords = read_data(path)
    stop_words = list()
    for word in stopwords:
        stop_words.append(word[:-1])
    return stop_words


def cut_words(data, stopwords):
    """
    分词、去停用词并将数据集分成训练集和测试集
    :param data: 文本数据
    :param stopwords: 停用词
    :param test_size: 测试集和训练集的划分比例
    :return: 测试集和训练集
    """
    y = list()
    text_list = list()
    for line in data:
        label, text = line.split('\t', 1)
        cut_text = [word for word in jieba.cut(text) if word not in stopwords]
        if cut_text == '':
            continue
        else:
            text_list.append(' '.join(cut_text))
            y.append(int(label))
    return text_list, y


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
    fpr, tpr, thresholds = sklearn.metrics.roc_curve(y, model.predict_proba(X)[:, 1], pos_label=1)
    return accuracy, sklearn.metrics.auc(fpr, tpr)

def predict_one_sentence(sentence, stop_words, model_lr_path, model_vectorizer_path):
    """
    获取输入的句子的特征词以及预测结果
    :param sentence: 输入的句子
    :param stop_words: 所有停止词的列表
    :param model_lr_path: lr模型存储路径
    :param model_vectorizer_path: vectorizer模型存储路径
    :return: 无
    """
    print("start one sentence")
    features = list()
    text_list = list()
    # cut sentence to words
    cut_text = [word for word in jieba.cut(sentence) if word not in stop_words]
    # connect all words with ' '
    if cut_text == '':
        return
    else:
        text_list.append(' '.join(cut_text))
    # load vectorizer model to get tf-idf features
    vectorizer = joblib.load(filename=model_vectorizer_path)
    sentence_tfidf = vectorizer.transform(text_list)
    # get corresponding name of feature
    feature_name = vectorizer.get_feature_names()
    sentence_array = sentence_tfidf.toarray()
    # order the sentence tfidf feature and get the three most special words
    features_index = pd.Series(sentence_array[0]).sort_values(ascending=False).index[:3]
    for i in features_index:
        features.append(feature_name[i])
    print(features)
    # use loaded model to predict the sentence
    lr = joblib.load(filename=model_lr_path)
    print(lr.predict(sentence_tfidf))
    print("end one sentence")


if __name__ == "__main__":
    # step1 读取数据（文本和停用词）
    data_path = "./data/train.txt"
    stopwords_path = "./data/stopwords.txt"
    model_lr_path = "./model/lr.model"
    model_vectorizer_path = "./model/vectorizer.model"
    data = read_data(data_path)
    stopwords = get_stop_words(stopwords_path)

    # 直接进行预测
    # sentence="浦发信用卡祝您生日快乐，如意安康！感谢您对浦发信用卡的支持。【浦发银行】"
    # predict_one_sentence(sentence, stopwords, model_lr_path, model_vectorizer_path)

    # step2 分词、分为训练集和测试集
    text_list, y = cut_words(data, stopwords)
    test_size = 0.2
    X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(text_list, y, test_size=test_size, random_state=1028)

    # step3 提取特征参数（tf-idf）
    X_train_tfidf, X_test_tfidf, tfidf_model, feature_name = calculate_tfidf(X_train, X_test)
    # print(feature_name)
    test_array = X_test_tfidf.toarray()
    features_index = pd.Series(test_array[0]).sort_values(ascending=False).index[:3]
    print(X_test[0])
    for i in features_index:
        print(feature_name[i])

    # step4 训练lr模型
    lr = LogisticRegression(C=1.0)
    lr.fit(X_train_tfidf, y_train)



    # step5 模型评估
    accuracy, auc = evaluate(lr, X_train_tfidf, y_train)
    print("训练集正确率：%.4f%%\n" % (accuracy * 100))
    print("训练集AUC值：%.6f\n" % auc)

    accuracy, auc = evaluate(lr, X_test_tfidf, y_test)
    print("测试集正确率：%.4f%%\n" % (accuracy * 100))
    print("测试AUC值：%.6f\n" % auc)
