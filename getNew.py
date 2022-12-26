
import requests

url = 'https://raw.githubusercontent.com/deezertidal/shadowrocket-rules/main/shadowrocket_basic.conf'

proxyaddr = "127.0.0.1"    
proxyport = 1081                     

proxyurl="http://"+proxyaddr+":"+"%d"%proxyport

r = requests.get(url,proxies={'http':proxyurl,'https':proxyurl},headers={
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate",
    "Accept-Language":"zh-CN,zh;q=0.9",
    "Cache-Control":"max-age=0",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"})

f = open('basic.conf','r')
str1 = f.read()
f.close()
str2 = r.text

i=str2.index('[Script]')
strNew = str1 + '' + str2[i:-1]

#print(strNew)
file=open('new.conf', 'w')
file.write(strNew)
file.close()
