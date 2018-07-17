# -*- coding:UTF-8 -*-
from urllib import request
from bs4 import BeautifulSoup
import chardet
import re
def download(urls):
    for item in urls:
        print(item[3] + ':' + 'http://www.biquge.com.tw' + item[1])
    sure = input("是否下载这些章节y/n（下载在当前目录下，访问上面链接可以直接观看）：")
    if sure == 'y' or sure == 'Y':
        for item in urls:
                f = open(item[3], mode='w+', encoding='utf-8')
                download_url = 'http://www.biquge.com.tw' + item[1]
                head = {}
                head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
                download_req = request.Request(url=download_url, headers=head)
                download_response = request.urlopen(download_req)
                download_html = download_response.read().decode('gbk', 'ignore')
                soup_texts = BeautifulSoup(download_html, 'lxml')
                texts = soup_texts.find_all(id="content")
                soup_text = BeautifulSoup(str(texts), 'lxml')
                f.write(soup_text.div.text.replace('\xa0', ''))
                f.close
                print(item[3]+" 下载完成\n")
    print('all down')
    return
def find_url(target_url):
    head = {}
    head[
        'User-Agent'] = "Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19"
    req = request.Request(url=target_url, headers=head)
    response = request.urlopen(req)
    html = response.read()
    code = chardet.detect(html)['encoding']
    html = html.decode('gbk')
    soup = BeautifulSoup(html, 'html.parser')
    result = re.findall('<a(.*?)href\=\"(.*?)\"(.*?)>(.*?)</a>', str(soup.find_all(id='list')))
    download(urls=result)
def search(txt_name):
    target_name = str(txt_name.encode("GBK")).upper()
    target_url = 'http://www.biquge.com.tw/modules/article/soshu.php?searchkey='
    i = 2
    while i < len(target_name) - 1:
        if target_name[i] == '\\':
            target_url += '%'
            i += 2
            continue
        target_url += target_name[i]
        i += 1
    head = {}
    head[
        'User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    req = request.Request(url=target_url, headers=head)
    html = request.urlopen(req)
    if target_url != html.geturl():
        print("已经找到,正在提取\n")
        target_url=html.geturl()
        find_url(target_url)
        return
    html = html.read().decode('GBK')
    result = re.finditer(r'<td class="odd"><a href="(.*?)">(.*?)</a>', html)
    flag = 0
    for item in result:
        if item[2] == txt_name:
            target_url = item[1]
            print("已经找到，正在提取\n")
            find_url(target_url=target_url)
            return
    print('找不到')
if __name__=='__main__':
    name = input("输入要找的小说名称：")
    search(txt_name=name)
