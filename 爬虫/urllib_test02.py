# -*- coding: UTF-8 -*-
from urllib import request

if __name__ == "__main__":
    req = request.Request("http://fanyi.baidu.com/")
    #url也可以是一个Request对象，这就需要我们先定义一个Request对象，然后将这个Request对象作为urlopen的参数使用，方法如下：
    response = request.urlopen(req)
    html = response.read()
    html = html.decode("utf-8")
    print(html)
