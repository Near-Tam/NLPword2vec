#coding:utf-8
from __future__ import division
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import time
import os
import jieba
import jieba.posseg as pseg


if __name__ == "__main__":
	jieba.load_userdict("AllMusicLibrary.txt")
	f = open("chinese.txt","r")
	num = len(f.readlines())
	f.close()
	f = open("chinese.txt","r")
	i = 0.
	t0 = time.time()
	print("-----start cut-----")
	while i<num:
		i = i + 1
		t1 = time.time()
		time_left = (num-i)*(t1-t0)/i
		m, s = divmod(time_left, 60)
		h, m = divmod(m, 60)
		os.system("clear")
		print("-----Completed: "+str(100*i/num)+"%-----")
		print("-----"+str(int(h))+"h "+str(int(m))+"min "+str(int(s))+"s-----")
		s = f.readline().decode('utf-8')
		words = pseg.cut(s)
		F = open("train.data.model","a")
		for word,flag in words:
			F.write(word + " ")
		F.close()	
