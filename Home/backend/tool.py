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
    with open(data_path, 'r') as f:
        reader = csv.reader(f)
        for item in reader:
            if reader.line_num == 1:
                continue
            text = item[1].lower()
            text = re.sub('https?://\S+|www\.\S+', '', text)
            text = re.sub('[^A-Za-z]+', ' ', text)
            data.append(''.join([word + ' ' for word in text.split() if word not in StopWords]))
    return data

