"""
@Author: lxy-146
@Description: 
@Filetype: test.py
@Time: 2022/6/16:22:17
"""
from nltk.corpus import stopwords
import re
StopWords = stopwords.words("english")
text = 'https://icons8.com/icons/set/cloud is a website to search for icons.'
text = text.lower()
text = re.sub('https://\S+|www\.\S+', '', text)
text = re.sub('[^A-Za-z]+', ' ', text)
text = ''.join([word + ' ' for word in text.split() if word not in StopWords])
print('text: ', text)