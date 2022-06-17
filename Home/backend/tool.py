"""
@Author: lxy-146
@Description: 
@Filetype: tool.py
@Time: 2022/6/17:14:00
"""
import re
import csv
import sklearn
from nltk.corpus import stopwords

def get_data_from_csv(data_path):
    StopWords = stopwords.words("english")
    data = []
    ground_truth = []
    origin = []
    with open(data_path, 'r') as f:
        reader = csv.reader(f)
        for item in reader:
            if reader.line_num == 1:
                continue
            origin.append(item[1])
            text = item[1].lower()
            text = re.sub('https?://\S+|www\.\S+', '', text)
            text = re.sub('[^A-Za-z]+', ' ', text)
            data.append(''.join([word + ' ' for word in text.split() if word not in StopWords]))
            ground_truth.append(item[2])
    return data, ground_truth, origin

def calculate_accuracy(result, ground_truth):
    l = len(result)
    t = 0
    for i in range(l):
        if result[i] == ground_truth[i]:
            t = t + 1
    accuracy = t / l
    return accuracy