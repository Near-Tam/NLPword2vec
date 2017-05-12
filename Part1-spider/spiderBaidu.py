#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

import os
import os
import urllib
import urllib2
from bs4 import BeautifulSoup

def gethtml(keyword):
        response = urllib2.Request("http://baike.sogou.com/v60469.htm?fromTitle={0}".format(keyword))
        response.add_header('User-Agent', 'chrome')
        response = urllib2.urlopen(response)
        html = response.read()
        #print(html)
        response.close()
        return html
def search_what(keywords):

    wd = urllib2.quote(keywords)
    url = 'http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&ch=12&tn=56060048_4_pg&wd='+wd
    url = url+'&rsv_pq=ff64d901000031d4&rsv_t=1b7cB%2FKAQLLDfettJz2WrartM10yMWFSwzgBoHAmYV2X6Dv3mqbDMJyJyfplrLpO%2BP8XKA&rsv_enter=1&rsv_sug3=5&rsv_sug1=4&rsv_sug2=0&inputT=6285&rsv_sug4=11467'

    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
               'Accept':'text/html;q=0.9,*/*;q=0.8',
               'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
               'Accept-Encoding':'gzip',
               'Connection':'close',
               'Referer':None #注意如果依然不能抓取的话，这里可以设置抓取网站的host
    }

    #pener = urllib2.Request.build_opener()

    #page = urllib2.Request.add_header("User-Agent","chrome").urlopen(url).read().decode('utf-8')
    page = urllib2.Request(url)
    page.add_header("User-Agent","chrome")
    page = urllib2.urlopen(page)
    Page = page.read().decode('utf-8')
    html = BeautifulSoup(Page)
    returnTest = ""
    for i in range(1,10):
        res = html.find(id=i)
        print('第',i,'条结果：')
        if res.h3 != None:
            print("Flag1:  "+res.h3.get_text(strip=True))
            returnTest = returnTest + res.h3.get_text(strip=True)
        elif res.h4 != None:
            print("Flag1:  "+res.h4.get_text(strip=True))
            returnTest = returnTest + res.h4.get_text(strip=True)
        #else:
            #print('无法提取标题')
        if res.find('div',class_='c-abstract') !=None:
            print("Flag2:  "+res.find('div',class_='c-abstract').get_text(strip=True))
            returnTest = returnTest + res.find('div',class_='c-abstract').get_text(strip=True)
        elif res.find('div',class_='c-span18') !=None:
            if res.find('div',class_='c-span18').p !=None:
                print("Flag3:   "+res.find('div',class_='c-span18').p.get_text(strip=True))
                returnTest = returnTest + res.find('div',class_='c-span18').p.get_text(strip=True)
            else:
                print("Flag4:   "+res.find('div',class_='c-span18').get_text(strip=True))
                returnTest = returnTest + res.find('div',class_='c-span18').get_text(strip=True)
        else:
            print('无法提取描述')
        if res.find('span',class_='g') != None:
            print('网站：',res.find('span',class_='g').get_text(strip=True).split('/')[0])
        elif res.find('p',class_='op-bk-polysemy-move') !=None:
            print('网站：',res.find('p',class_='op-bk-polysemy-move').get_text(strip=True).split('/')[0])
        #else:
            #print('无法提取网址')
        print('\n')
    return returnTest+"\n"

if __name__ == "__main__":
	keyWordDataFile = open("AllMusicLibrary.txt","r")
	keyWordData = keyWordDataFile.read()
	keyWordData = keyWordData.replace("\n","")
	keyWordData = keyWordData.replace("100 wkz","")
	keyWordData = keyWordData.split(" ")
	keyWordDataFile.close()
	i = 0
	Error = ""
	f = open("baiduData.txt","w")
	for keyword in keyWordData:	
		#f = open("log.txt","w+")
		i = i+1
		os.system("clear")
		print(str(i)+"/"+str(len(keyWordData)))
		print(keyword)
		print("Error:" + Error)
		try:
			html = search_what(keyword)
			f.write(html)
		except:
			print("Error")
			Error = Error + ", " + keyword
		
	f.close()
