# -*- coding: utf-8 -*-

"""
# @Author   : Gary Ding
# @Time     : 2022-05-05 23:39
# @File     : Personal_try.py
# @Project  : Tweet_Project
"""

from mittens import GloVe
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler


# cooccurrence = np.array([
#     [  4.,   4.,   2.,   0.],
#     [  4.,  61.,   8.,  18.],
#     [  2.,   8.,  10.,   0.],
#     [  0.,  18.,   0.,   5.]])
# glove_model = GloVe(n=2, max_iter=300)
# embeddings = glove_model.fit(cooccurrence)
#
# print('\nembeddings:')
# print(embeddings)

# df = pd.DataFrame({'a': [1, 3, 5, 7, 4, 5, 6, 4, 7, 8, 9], 'b': [3, 5, 6, 2, 4, 6, 7, 8, 7, 8, 9]})
# print(df)
# print()
# print(df.values.tolist())

# a=[]
# b=[1,2,3]
# a+=b
# print(a)

X_train=np.genfromtxt('feaM_bert.csv',delimiter=',')
for item in X_train:
    print(np.mean(item))

# 进行归一化
scalar=MinMaxScaler()
feaN=scalar.fit_transform(X_train)
print('现在')
for item in X_train:
    print(np.mean(item))

