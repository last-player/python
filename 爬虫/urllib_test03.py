# -*- coding: UTF-8 -*-
from urllib import request

if __name__ == "__main__":
    req = request.Request("http://www.jxust.edu.cn/")
    response = request.urlopen(req)
    #返回的是一个url的字符串；
    print("geturl打印信息："+str(response.geturl()))
    print('**********************************************')
    #返回的是一些meta标记的元信息，包括一些服务器的信息；
    print("info打印信息："+str(response.info()))
    print('**********************************************')
    #返回的是HTTP的状态码，如果返回200表示请求成功。
    print("getcode打印信息："+str(response.getcode()))
