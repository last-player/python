# -*- coding: UTF-8 -*-
from urllib import request
import chardet

if __name__ == "__main__":
    response = request.urlopen("http://fanyi.baidu.com/")
    html = response.read()
    charset = chardet.detect(html)
    txt=html.decode(charset['encoding'])
    #自动识别编码,返回一个字典
    print(charset)
    print(txt)
