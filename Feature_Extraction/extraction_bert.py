from vocab_creation import Vocab
from extraction_glove import load_vocab
from utils import list2csv

from bert_serving.client import BertClient
bc = BertClient(ip='10.60.38.173',check_length=False)

if __name__=="__main__":
    lines,corpus,vocab=load_vocab()
    for i in range(len(lines)):
        if lines[i]=="":
            print(i)
    doc_vecs = bc.encode(lines)
    print('矩阵测试：', doc_vecs.shape)
    print(doc_vecs)
    list2csv('feaM_bert_2.csv',doc_vecs)