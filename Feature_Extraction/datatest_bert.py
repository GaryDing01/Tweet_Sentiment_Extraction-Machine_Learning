from utils import list2csv
from vocab_creation import read_lines

from extraction_glove import load_vocab
from bert_serving.client import BertClient
bc = BertClient(ip='10.60.38.173',check_length=False)

if __name__ == "__main__":
    lines = read_lines('../Data/test_1.csv')
    doc_vecs = bc.encode(lines)
    print('矩阵测试：', doc_vecs.shape)
    print(doc_vecs)
    list2csv('test_bert_2.csv', doc_vecs)