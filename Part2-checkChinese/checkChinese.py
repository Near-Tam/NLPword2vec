#-*-coding:utf-8-*-
import sys
reload(sys)
sys.setdefaultencoding("utf8")

import time
import os

def is_chinese(uchar):
        """判断一个unicode是否是汉字"""
        if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
                return True
        else:
                return False


if __name__ == "__main__":
	f = open("baiduData.txt","r")
	num = len(f.readlines())
	f.close()
	f = open("baiduData.txt","r")
	i = 0.
	t0 = time.time()
	while i<num:
		os.system("clear")
		i = i+1
		t1 = time.time()
		detaT = t1-t0
		time_left = (num-i)*detaT/i
		m, s = divmod(time_left, 60)
		h, m = divmod(m, 60)
		print("Process: "+str(100*i/num)+"%")
                print(str(h)+"h "+str(m)+"min "+str(s)+"s")
		s = f.readline().decode("utf-8")
		for si in s:
			if is_chinese(si) == True:
				F = open("chinese.txt","a")
				F.write(si)
				F.close()		

	f.close()
