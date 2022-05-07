# -*- coding: utf-8 -*-

"""
# @Author   : Gary Ding
# @Time     : 2022-05-06 10:49
# @File     : vocab_creation.py
# @Project  : Tweet_Project
"""

import collections
import re
# from d2l import torch as d2l
import pandas as pd
import pickle


def read_lines(content_filepath, content_type=None):
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

    # 把不是大写字母和小写字母的全部变成空格，暂时不变成小写!!!
    for i in range(len(lines)):
        if isinstance(lines[i], str) == False:
            print(i, lines[i])
            exit()

    return [re.sub('[^A-Za-z]+', ' ', line).strip() for line in lines]


def tokenize(lines, token='word'):
    '''
    # 将文本行拆分为单词或字符标记
    # 单词，中文的话比较麻烦
    :param lines: 带空格的语句
    :param token: 选择的拆分方式:word或者char
    :return: 拆分后的词语列表
    '''
    if token == "word":
        return [line.split() for line in lines]
    # 字符标记
    if token == "char":
        return [list(line) for line in lines]
    else:
        print("错误，未知令牌类型：" + token)


def count_corpus(tokens):
    '''
    # 统计标记的频率
    :param tokens:
    :return:
    '''
    if len(tokens) == 0 or isinstance(tokens[0], list):
        tokens = [token for line in tokens for token in line]
    return collections.Counter(tokens)  # Counter是一个字典类，返回的就是计数字典


class Vocab:
    '''
    # 文本词汇表
    # 把字符串转换成一个下标
    '''

    def __init__(self, tokens=None, min_freq=0, reserved_tokens=None):
        if tokens is None:
            tokens = []
        if reserved_tokens is None:
            reserved_tokens = []
        counter = count_corpus(tokens)
        self.token_fregs = sorted(counter.items(), key=lambda x: x[1], reverse=True)  # 按照词频进行排序
        self.unk, unig_tokens = 0, ['<unk'] + reserved_tokens  # 先加入未知词这一类
        # 构建词语表
        unig_tokens += [
            token for token, freq in self.token_fregs
            if freq >= min_freq and token not in unig_tokens
        ]
        self.idx_to_token, self.token_to_idx = [], dict()
        for token in unig_tokens:
            self.idx_to_token.append(token)
            self.token_to_idx[token] = len(self.idx_to_token) - 1

    def __len__(self):
        return len(self.idx_to_token)

    def __getitem__(self, tokens):  # 可以用vocab[tokens]取对应的key值
        if not isinstance(tokens, (list, tuple)):
            return self.token_to_idx.get(tokens, self.unk)  # 默认是不知道的词
        return [self.__getitem__(token) for token in tokens]  # 如果查找多于一个数值，则返回所有符合条件的List

    def to_tokens(self, indices):  # 返回key对应的token或者token序列
        if not isinstance(indices, (list, tuple)):
            return self.idx_to_token[indices]
        return [self.idx_to_token[index] for index in indices]


# 读进一个按char分的文本，把整个文本的char都map成一个下标，构建一个词汇表
def load_corpus_content(max_token=-1):
    '''
    # 返回Time Machine数据集的标记索引列表和词汇表
    :param max_token:
    :return: corpus: 一共有多少次出现的词语, vocab：一共有多少个不同的词语
    '''

    lines = read_lines('../Data/small_train.csv')  # 序号314无推特文字信息
    # lines=["you and i it's you and I I don't care and it will be you who is always with me"]
    with open('./lines.data', 'wb') as file:
        pickle.dump(lines, file)
    tokens = tokenize(lines, "word")

    vocab = Vocab(tokens)  # 构建完成的词汇表
    corpus = vocab[tokens]
    # if max_token > 0:
    #     corpus = corpus[:max_token]
    return corpus, vocab


if __name__ == "__main__":
    corpus, vocab = load_corpus_content()  # 每一个corpus对应的是一个token
    print("使用整体的训练集验证：")
    print('len(corpus):', len(corpus))
    print('len(vocab):', len(vocab))
    print('corpus:', corpus)
    print('vocab:', vocab.token_to_idx.items())
    print('get_item:',vocab['for','me'])
    print('to_token:',vocab.to_tokens([1,2,3]))

    # with open('./corpus.data', 'wb') as file:
    #     pickle.dump(corpus, file)
    # with open('./vocab.data', 'wb') as file:
    #     pickle.dump(vocab, file)
    #
    # with open('./vocab.data', 'rb') as file:
    #     new_vocab = pickle.load(file)
    # print('len(new_vocab)', len(new_vocab))
