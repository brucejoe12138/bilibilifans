import requests
import time
from bs4 import BeautifulSoup
import json


#标记网址
url="https://api.bilibili.com/x/relation/stat?vmid=777536"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'}
#标记程序开始时的粉丝数
soup = requests.get(url, headers=headers)
val = BeautifulSoup(soup.text, 'lxml')
sub = 0                         #5秒内取关人数
num1 = int(val.p.string[-9:-2]) #5秒前关注人数


#无限循环 计算实时粉丝数据，与前5秒的差值（取关人数），记录进txt文件中
var = 1
while var == 1 :
    f = open("record.txt", 'a')
    soup = requests.get(url, headers=headers)
    val = BeautifulSoup(soup.text, 'lxml')
    number = int(val.p.string[-9:-2])             #当前关注人数
    sub = num1 - number
    print('粉丝：'+val.p.string[-9:-2]+'   取关人数：  '+str(sub))
    num1 = number
    f.write(time.strftime("%Y-%m-%d %H:%M:%S ",time.localtime(time.time()))+'   lexburner粉丝数：'+val.p.string[-9:-2]+'    5秒内取关人数'+str(sub)+'\n')
    f.close()
    time.sleep(5)

    #numbers = val.p.string[-9:-2]
    #filename = "record.json"
    #with open(filename, 'a') as file_obj:
    #    json.dump(numbers, file_obj)
    #file_obj.close()



