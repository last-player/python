# -*- coding: UTF-8 -*-
from urllib import request
import re
if __name__=='__main__':
    txt_name=input("输入要找的小说名称：")
    target_name=str(txt_name.encode("GBK")).upper()
    target_url='http://www.biquge.com.tw/modules/article/soshu.php?searchkey='
    i=2
    while i<len(target_name)-1:
        if target_name[i]=='\\':
            target_url+='%'
            i+=2
            continue
        target_url+=target_name[i]
        i+=1
    head={}
    head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    req=request.Request(url=target_url,headers=head)
    html=request.urlopen(req)
    target_url=html.geturl()
    html=html.read().decode('GBK')
    result=re.finditer(r'<td class="odd"><a href="(.*?)">(.*?)</a>',html)
    flag=0
    for item in result:
        if item[2]==txt_name:
            target_url=item[1]
            print(target_url)