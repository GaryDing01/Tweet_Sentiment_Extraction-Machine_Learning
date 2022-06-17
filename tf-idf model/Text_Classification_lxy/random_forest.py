"""
@Author: lxy-146
@Description: 
@Filetype: random_forest.py
@Time: 2022/5/28:21:48
"""
from sklearn import tree
import numpy as np

class RandomForest(object):
    def __init__(self, tree_num):
        if tree_num <= 0:
            print('The number of trees must be greater than 0!!')
            return
        self.tree_num = tree_num
        self.trees = []
        self.sampling_rate = 0.8
        self.feature_rate = 0.6
        for i in range(tree_num):
            self.trees.append(tree.DecisionTreeClassifier())

    def fit(self, x_train, y_train):
        total_samples_num, total_feature_num = x_train.shape
        for tree_index in range(self.tree_num):
            print('tree index:', tree_index)
            bootstrapping = []
            for i in range(int(self.sampling_rate * total_samples_num)):
                bootstrapping.append(np.floor(np.random.random() * total_samples_num))
            labels = []
            for i in range(len(bootstrapping)):
                print('bootstraping: ', i)
                if i == 0:
                    samples = x_train[int(bootstrapping[i])].toarray()
                else:
                    samples = np.row_stack((samples, x_train[int(bootstrapping[i])].toarray()))
                labels.append(y_train[int(bootstrapping[i])])
            self.trees[tree_index].fit(samples, labels)
        print('random forest fit finish')

    def score(self, x_test, y_test):
        result = []
        for i in range(self.tree_num):
            result.append(self.trees[i].predict(x_test))
        tmp_label = {}
        final_result = []
        for i in range(len(y_test)):
            tmp_label.clear()
            for j in range(self.tree_num):
                if result[j][i] not in tmp_label.keys():
                    tmp_label[result[j][i]] = 0
                tmp_label[result[j][i]] = tmp_label[result[j][i]] + 1
            max_label = ''
            max_label_num = 0
            for key, value in tmp_label.items():
                if value > max_label_num:
                    max_label_num = value
                    max_label = key
            final_result.append(max_label)
        correct_sample_num = 0
        for i in range(len(y_test)):
            if final_result[i] == y_test[i]:
                correct_sample_num = correct_sample_num + 1
        return correct_sample_num / len(y_test)




