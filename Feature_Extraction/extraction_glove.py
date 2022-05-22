# -*- coding: utf-8 -*-

"""
# @Author   : Gary Ding
# @Time     : 2022-05-05 23:25
# @File     : extraction_glove.py
# @Project  : Tweet_Project
"""

import numpy as np
from mittens import GloVe
import pickle
import datetime
import copy

from vocab_creation import Vocab
from utils import MaxMinNormalization,list2csv

from sklearn.decomposition import PCA
# from sklearn.preprocessing import MinMaxScaler


# # 一个小例子
# # 初始化模型
# vecLength=100           # 矩阵长度
# max_iter=100000         # 最大迭代次数
# display_progress=1000   # 每次展示
# glove_model = GloVe(n=vecLength, max_iter=max_iter, display_progress=display_progress)
# # 模型训练与结果输出
# # embeddings = glove_model.fit(coocMatric)

def load_vocab():
    '''
    导入相关数据
    :return: 返回所有vocab创建过程中的重要信息. 感觉corpus就是Glove需要的输入
    '''
    with open('./lines.data', 'rb') as file:
        lines = pickle.load(file)
    with open('./corpus.data', 'rb') as file:
        corpus = pickle.load(file)
    with open('./vocab.data', 'rb') as file:
        vocab = pickle.load(file)
    return lines, corpus, vocab


def create_cooccurrence(data, coWindow=3, tableSize=1000):
    '''
    创建共现矩阵
    :param coWindow: 共现窗口大小
    :param tabelSize: 共现矩阵维度
    :return:
    '''
    cooccurrence = np.zeros((tableSize, tableSize), dtype=int)  # 初始化共现矩阵

    def countCOOC(cooccurrence, window, coreIndex):
        '''
        统计移动窗口内部的共现
        :param cooccurrence: 当前共现矩阵
        :param window: 当前移动窗口数组
        :param coreIndex: 当前移动窗口数组中的窗口中心位置，也就是基准词
        :return:
        '''
        for index in range(len(window)):
            if index == coreIndex:
                continue
            else:
                cooccurrence[window[coreIndex]][window[index]] += 1
        return cooccurrence

    # 开始统计
    flag = 0
    startTime = datetime.datetime.now()
    for item in data:
        itemInt = [int(x) for x in item]
        for core in range(1, len(item)):
            if core <= coWindow + 1:
                # 左窗口不足
                window = itemInt[1:core + coWindow + 1]
                coreIndex = core - 1
                cooccurrence = countCOOC(cooccurrence, window, coreIndex)
            elif core >= len(item) - 1 - coWindow:
                # 右窗口不足
                window = itemInt[core - coWindow:(len(item))]
                coreIndex = coWindow
                cooccurrence = countCOOC(cooccurrence, window, coreIndex)
            else:
                # 左右均没有问题
                window = itemInt[core - coWindow:core + coWindow + 1]
                coreIndex = coWindow
                cooccurrence = countCOOC(cooccurrence, window, coreIndex)
        flag = flag + 1
        if flag % 1000 == 0:
            endTime = datetime.datetime.now()
            print("已经计算了%s条数据，用时%s" % (flag, endTime - startTime))

    # print(cooccurrence)
    return cooccurrence


# 使用GloVe生成词向量
def complete_glove2vec(cooccurrence, max_iter=300):
    # n=cooccurrence.shape[0]
    vec_len=int(8.33*np.log10(cooccurrence.shape[0]))+1
    glove_model = GloVe(n=vec_len, max_iter=max_iter)
    # 保存模型
    with open('./glove.data', 'wb') as file:
        pickle.dump(glove_model, file)
    print('保存模型成功！')
    # 模型训练与结果输出
    embeddings = glove_model.fit(cooccurrence)
    # print('\nembeddings:')
    # print(embeddings)
    # print(embeddings.shape)

    # 保存glove模型，返回embeddings结果
    return embeddings

# 拼成特征矩阵
def create_featureMatrix(corpus,embeddings,pca_components=30):
    # 先按照词向量创建特征列表
    feaL=[[] for i in range(len(corpus))]
    vec_len=embeddings.shape[1]

    for i in range(len(feaL)):
        for j in range(len(corpus[i])):
            feaL[i].append(list(embeddings[corpus[i][j]]))

    def calc_meanlist(l1):
        l2=[]
        a1=np.array(l1).T
        # print(a1.shape)
        for i in range(a1.shape[0]):
            l2.append(np.mean(a1[i]))
        return l2

    print('在这里测试')
    feaS=[[] for i in range(len(corpus))]
    for i in range(len(feaL)):
        feaS[i]+=calc_meanlist(feaL[i])
    list2csv('firstversion.csv',feaS)

    feaM=np.array(feaS)
    print(feaM.shape)
    # print(feaM)
    exit()

    # 此时每一个样本特征数量不一样，需要进行特征选择
    # !!!需要标记选出来的特征原来是来自哪个词的
    # # 进行归一化
    # scalar=MinMaxScaler()
    # feaN=scalar.fit_transform(feaL)

    # 只能自己进行归一化
    for item in feaL:
        item=MaxMinNormalization(item)

    print(feaL)
    print(len(feaL))
    print(len(feaL[0]))
    print('小测试')
    for item in feaL:
        print(len(item))

    # # PCA降维
    # pca = PCA(n_components=pca_components)  # 主成分数量为2，方便可视化
    # for item in feaL:
    #     item=pca.fit_transform([item])[0]
    # print('测试')
    # print(feaL)
    # print(len(feaL))
    # print(len(feaL[0]))



if __name__ == "__main__":
    lines, corpus, vocab = load_vocab()
    print('len(lines):', len(lines))
    print('len(corpus):',len(corpus))
    print('len(vocab):',len(vocab))
    print(lines)
    # # print("corpus:",corpus)
    # # exit()
    # cooccurrence=create_cooccurrence(corpus,tableSize=len(vocab))
    # print('\nAbout cooccurrence:',cooccurrence.shape)
    # # print('cooccurrence:')
    # # print(cooccurrence)
    #
    # embeddings=complete_glove2vec(cooccurrence)
    # print()
    # create_featureMatrix(corpus,embeddings)
