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

from vocab_creation import Vocab


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


if __name__ == "__main__":
    lines, corpus, vocab = load_vocab()
    print('len(corpus):',len(corpus))
    print('len(vocab):',len(vocab))
    cooccurrence=create_cooccurrence(corpus,tableSize=len(vocab))
    print('About cooccurrence:',cooccurrence.shape)

    max_iter=200         # 最大迭代次数
    display_progress=1000   # 每次展示
    glove_model = GloVe(n=cooccurrence.shape[0], max_iter=max_iter, display_progress=display_progress)
    # 模型训练与结果输出
    embeddings = glove_model.fit(cooccurrence)
    print('embeddings:')
    print(embeddings)
    print(embeddings.shape)
