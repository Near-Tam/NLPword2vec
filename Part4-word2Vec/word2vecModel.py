#-*-coding:utf-8-*-
from gensim.models import word2vec
from gensim.models import word2vec as LineSentence

import logging

import sys
reload(sys)
sys.setdefaultencoding('utf8')

if __name__ == "__main__":
	logging.basicConfig(format='%(asctime)s:%(levelname)s:(message)s',level=logging.INFO)
	txt = word2vec.Text8Corpus(u'train.data.model')
	model = word2vec.Word2Vec(txt,size=100,window=50,min_count=1)
	model.save('word2vec.model')
