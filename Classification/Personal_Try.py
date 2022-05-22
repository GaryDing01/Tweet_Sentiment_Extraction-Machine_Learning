import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler

# X = np.array([[0, 1], [2, 3], [4, 5], [6, 7]])
# print(X)
# y = np.array([1, 2, 3, 4])
# clf = SVC()
# SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
#     decision_function_shape='ovr', degree=3, gamma='auto', kernel='rbf',
#     max_iter=-1, probability=False, random_state=None, shrinking=True,
#     tol=0.001, verbose=False)
# clf.fit(X, y)
# print(clf.predict([[1.1, 0.9]]))

# li = load_iris ( )
# x_train , x_test , y_train , y_test = train_test_split ( li.data , li.target , test_size = 0.25 )
# stand = StandardScaler ( )
# x_test = stand.fit_transform ( x_test )
# x_train = stand.transform ( x_train )
# #当调用网格搜索进行调参的时候，不要在被调参函数里写参数了
# knn = KNeighborsClassifier ( )
# # 构造一些参数的值进行搜索,参数名一定要写对啊：
# pargam = {"n_neighbors" : [1,2,3 , 4 , 5]}
# #网格搜索里面有下面两个函数的功能，就不需要再写了，网格搜索相当于把目标函数包含了
# # knn.fit ( x_train , y_train )
# # y_predict = knn.predict ( x_test )
# gc=GridSearchCV(knn,param_grid = pargam,cv=2)
# gc.fit( x_train , y_train )
# print ( '在测试集上准确率：' , gc.score ( x_test , y_test ) )
# print('在交叉验证中最好的结果：',gc.best_score_)
# print ( '选择最好的模型：' , gc.best_estimator_)
# print ( '每个超参数每次交叉验证的结果：' , gc.cv_results_ )

# from nltk.tokenize import wordpunct_tokenize
#
# if __name__ == "__main__":
#     s = '''Good muffins cost $3.88\nin New York.  Please buy me
#     ... two of them.\n\nThanks.'''
#     print(wordpunct_tokenize(text=s))  # 分词

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

# nltk.download()

example_sent = "This is a sample sentence, showing off the stop words filtration."

stop_words = set(stopwords.words('english'))

word_tokens = word_tokenize(example_sent)

filtered_sentence = [w for w in word_tokens if not w in stop_words]

print(word_tokens)
print(filtered_sentence)

