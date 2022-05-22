from sklearn.feature_extraction.text import CountVectorizer

from vocab_creation import Vocab
from extraction_glove import load_vocab
from utils import list2csv

if __name__=="__main__":
    lines,corpus,vocab=load_vocab()
    for i in range(len(lines)):
        if lines[i]=="":
            print(i)
    cv = CountVectorizer()
    doc_vecs = cv.fit_transform(lines).toarray()
    print('矩阵测试：', doc_vecs.shape)
    print(doc_vecs)
    list2csv('feaM_countv.csv',doc_vecs)