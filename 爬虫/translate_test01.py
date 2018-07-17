# -*- coding: UTF-8 -*-
from urllib import request
from urllib import parse
import json
if __name__ == "__main__":
    Request_URl='http://fanyi.youdao.com/translate'
    From_data={}
    From_data['doctype']='json'
    From_data['i']=input("输入要翻译的内容:")

    data=parse.urlencode(From_data).encode('utf-8')
    response=request.urlopen(Request_URl, data)
    html=response.read().decode('utf-8')
    translate_results = json.loads(html)
    type(translate_results)
    # 找到翻译结果
    translate_results = translate_results['translateResult'][0][0]['tgt']
    # 打印翻译信息
    print("翻译的结果是：%s" % translate_results)