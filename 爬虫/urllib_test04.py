# -*- coding: UTF-8 -*-
from urllib import request
from urllib import error
if __name__=="__main__":
    url=input("要访问的网址：")
    req=request.Request(url)
    try:
        response=request.urlopen(req)
        htm=response.read().decode('utf-8')
        print(htm)
    except error.HTTPError as e:
        #服务器正确但是没有那个资源
        print(e.code)
    except error.URLError as e:
        #服务器不存在
        print(e.reason)
