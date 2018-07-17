# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
if __name__=="__main__":
    html = """
    <html>
    <head>
    <title>Jack_Cui</title>
    </head>
    <body>
    <p class="title" name="blog"><b>My Blog</b></p>
    <li><!--注释--></li>
    <a href="http://blog.csdn.net/c406495762/article/details/58716886" class="sister" id="link1">Python3网络爬虫(一)：利用urllib进行简单的网页抓取</a><br/>
    <a href="http://blog.csdn.net/c406495762/article/details/59095864" class="sister" id="link2">Python3网络爬虫(二)：利用urllib.urlopen发送数据</a><br/>
    <a href="http://blog.csdn.net/c406495762/article/details/59488464" class="sister" id="link3">Python3网络爬虫(三)：urllib.error异常</a><br/>
    </body>
    </html>
    """
    soup=BeautifulSoup(html,'lxml')
    # 全打印
    #print (soup.prettify())
    #打印标签
    #print(soup.title)
    #print(soup.head)
    #print(soup.html)
    #只打印标签里面的内容
    #print(type(soup.li.string))
    print(soup.body.contents)
    #注意换行符占一个位置，contents是列表
    print(soup.body.contents[1])
    #这是一个生成器
    for child in soup.body.children:
        print(child)