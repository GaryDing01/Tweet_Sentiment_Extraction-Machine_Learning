import numpy as np
import pandas as pd

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV,cross_validate

# Classifier
from sklearn.multiclass import OneVsRestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import LinearSVC
from sklearn import svm
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

from imblearn.over_sampling import SMOTE, ADASYN, BorderlineSMOTE

from sklearn.metrics import roc_curve, auc, roc_auc_score, precision_score, recall_score, f1_score, \
    classification_report, accuracy_score

# Visualizing
import matplotlib.pyplot as plt


# 处理训练集和测试集
def read_label(content_filepath, content_type=None):
    '''
    读进文本并进行初始信息转换
    :param content_filepath:
    :return:
    '''
    # 使用pandas读取特定列，并转换成list
    if content_type is None:
        content_type = ['text']
    lines_0 = pd.read_csv(content_filepath, usecols=content_type).values.tolist()
    lines = [i for j in lines_0 for i in j]
    labelM = np.zeros((len(lines),), dtype=str)
    for i in range(len(lines)):
        if lines[i] == 'neutral':
            labelM[i] = '0'
        elif lines[i] == 'positive':
            labelM[i] = '1'
        elif lines[i] == 'negative':
            labelM[i] = '2'

    return labelM


# 训练集
stand = StandardScaler()

X_train = np.genfromtxt('../Feature_Extraction/feaM_bert_2.csv', delimiter=',')
y_train = read_label('../Data/train_all.csv', ['sentiment'])

# # 这里用SMOTE试试看
# #SMOTE
# sm = SMOTE({'0':13500,'1':13500,'2':13500},random_state=42)
# # 采用SMOTE算法对少数类样本进行增强后的数据集
# X_train, y_train = sm.fit_resample(X_train, y_train)
# # print('Resampled dataset shape %s' % Counter(y_res))

X_train = stand.fit_transform(X_train)

# 测试集
X_test = np.genfromtxt('../Feature_Extraction/test_bert_2.csv', delimiter=',')
X_test = stand.transform(X_test)
y_test = read_label('../Data/test_1.csv', ['sentiment'])

print('Data prepared.\n')

def Vis(test, pred):
    # Matplotlib Visualization
    # Tip: Using Scatter Figure
    temp_test = test.astype(float)
    temp_pred = pred.astype(float)
    x = np.arange(1, 39)
    # y=np.arange(1,39)
    y1 = temp_test
    y2 = temp_pred
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    # 设置标题
    ax1.set_title('Classifier')
    # 设置X轴坐标
    plt.xlabel('Testing Sample')
    # 设置Y轴坐标
    plt.ylabel('Prediction')
    # 画散点图

    # print(temp_test.shape)
    ax1.scatter(x, y1, c='r', marker='x')
    ax1.scatter(x, y2, c='b', marker='s')
    # 显示所画的图
    plt.show()


def my_Vis(X_test, y_test, y_pred, subplot, Classifier):
    feaM = X_test

    fea_red = []
    fea_blue = []
    fea_green = []

    for i in range(len(y_pred)):
        if y_pred[i] == 0:
            fea_red.append(list(feaM[i]))
        elif y_pred[i] == 1:
            fea_blue.append(list(feaM[i]))
        elif y_pred[i] == 2:
            fea_green.append(list(feaM[i]))

    ax1 = plt.subplot()
    # 设置标题
    ax1.set_title(Classifier)
    # 设置X轴坐标
    plt.xlabel('Feature1')
    # 设置Y轴坐标
    plt.ylabel('Feature2')
    # 画散点图

    # print(temp_test.shape)
    ax1.scatter(np.array(fea_red)[:, 0], np.array(fea_red)[:, 1], c='r', marker='s')
    ax1.scatter(np.array(fea_blue)[:, 0], np.array(fea_blue)[:, 1], c='b', marker='s')
    ax1.scatter(np.array(fea_green)[:, 0], np.array(fea_green)[:, 1], c='g', marker='s')


def tryKNN(X_train, X_test, y_train, y_test):
    # KNN Inplementation
    neigh = KNeighborsClassifier()
    pargam = {"n_neighbors": [3, 5, 7, 9, 11]}
    print('KNN Starts Validating...')
    neigh.fit(X_train, y_train)

    gc = GridSearchCV(neigh, param_grid=pargam, cv=5)

    gc.fit(X_train, y_train)
    print('在测试集上准确率：', gc.score(X_test, y_test))
    print('在交叉验证中最好的结果：', gc.best_score_)
    print('选择最好的模型：', gc.best_estimator_)
    # print('每个超参数每次交叉验证的结果：', gc.cv_results_)

    # print('KNN Starts Training...')
    # train_result = neigh.predict(X_train)
    # precision = accuracy_score(train_result, y_train)
    # print('KNN Training precision: ', precision)
    #
    # print('KNN Starts Testing...')
    # test_result = neigh.predict(X_test)
    # precision = accuracy_score(test_result, y_test)
    # print('KNN Testing precision: ', precision)


def tryLogistic(X_train, X_test, y_train, y_test):
    # Logistic Regression Inplementation
    lgr = LogisticRegression(random_state=0)
    print('Logistic Starts Fitting...')
    lgr.fit(X_train, y_train)

    print('Logistic Starts Training...')
    train_result = lgr.predict(X_train)
    precision = accuracy_score(train_result, y_train)
    print('Logistic Training precision: ', precision)

    print('Logistic Starts Testing...')
    test_result = lgr.predict(X_test)
    precision = accuracy_score(test_result, y_test)
    print('Logistic Testing precision: ', precision)


def tryDecisionTree(X_train, X_test, y_train, y_test):
    # Decision Tree Inplementation
    dt = DecisionTreeClassifier(random_state=0)
    print('DecisionTree Starts Fitting...')
    dt.fit(X_train, y_train)

    print('DecisionTree Starts Training...')
    train_result = dt.predict(X_train)
    precision = accuracy_score(train_result, y_train)
    print('DecisionTree Training precision: ', precision)

    print('DecisionTree Starts Testing...')
    test_result = dt.predict(X_test)
    precision = accuracy_score(test_result, y_test)
    print('DecisionTree Testing precision: ', precision)


def tryRandomForest(X_train, X_test, y_train, y_test):
    # Random Forest Inplementation
    random_forest = RandomForestClassifier(n_estimators=100, min_samples_leaf=1,max_depth=8,max_features=10)
    print('RandomForest Starts Fitting...')
    random_forest.fit(X_train, y_train)

    print('RandomForest Starts Training...')
    train_result = random_forest.predict(X_train)
    precision = accuracy_score(train_result, y_train)
    print('RandomForest Training precision: ', precision)

    print('RandomForest Starts Testing...')
    test_result = random_forest.predict(X_test)
    precision = accuracy_score(test_result, y_test)
    print('RandomForest Testing precision: ', precision)


# # call predict
# y_pred = Predict('SVM', X_test)
# print("Test set predictions:\n {}".format(y_pred))
# print("Test set score: {:.4f}".format(np.mean((y_pred == y_test))))


def trySVM(X_train, X_test, y_train, y_test):
    # classifier = OneVsRestClassifier(svm.SVC(kernel='rbf'))
    classifier = svm.SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
                         decision_function_shape='ovr', degree=3, gamma='auto', kernel='rbf',
                         max_iter=-1, probability=False, random_state=None, shrinking=True,
                         tol=0.001, verbose=False)
    print('SVM Starts Fitting...')
    classifier.fit(X_train, y_train)

    # Test on Training data
    print('SVM Starts Training...')
    train_result = classifier.predict(X_train)
    precision = accuracy_score(train_result, y_train)
    print('SVM Training precision: ', precision)

    # Test on test data
    print('SVM Starts Testing...')
    test_result = classifier.predict(X_test)
    precision = accuracy_score(test_result, y_test)
    print('SVM Test precision: ', precision)

    # 和准确率是一样的
    # print(classifier.score(X_train,y_train))

    # y_score = classifier.decision_function(X_test)
    # print('roc_auc_score：', roc_auc_score(y_test, y_score, average="samples",multi_class="ovr"))  #svm


if __name__ == "__main__":
    tryKNN(X_train, X_test, y_train, y_test)
