# -*- coding: UTF-8 -*-
from urllib import request
if __name__=="__main__":
    url='http://www.whatismyip.com.tw/'
    head={}
    #写入user agent
    head['user agent']='Mozilla/5.0 (Android; Mobile; rv:14.0) Gecko/14.0 Firefox/14.0'
    #两种修改user agent的方法，不该就是默认python的会被屏蔽
    req=request.Request(url,headers=head)
    req=request.Request(url)
    req.add_header('user agent','Mozilla/5.0 (Android; Mobile; rv:14.0) Gecko/14.0 Firefox/14.0')
    response=request.urlopen(req)
    print(response.read().decode('utf-8'))