
import requests
import subprocess


save_path = "./new"

url = 'https://raw.githubusercontent.com/deezertidal/shadowrocket-rules/main/shadowrocket_basic.conf'

# 使用wget命令下载文件
subprocess.call(["wget", url, "-P", save_path])               

f = open('basic.conf','r')
str1 = f.read()
f.close()
f = open('new),'r')
str2 = r.read()
f.close()

i=str2.index('[Script]')
strNew = str1 + '' + str2[i:-1]

#print(strNew)
file=open('new.conf', 'w')
file.write(strNew)
file.close()
