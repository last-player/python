# -*- coding: UTF-8 -*-
from urllib import request

if __name__ == "__main__":
    response = request.urlopen("http://fanyi.baidu.com")
    #urllib使用使用request.urlopen()打开和读取URLs信息，返回的对象response如同一个文本对象
    html = response.read()
    #用read()读取
    html=html.decode("utf-8")
    #decode解码
    print(html)
