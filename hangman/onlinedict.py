#!/usr/bin/env python3
from bs4 import BeautifulSoup
import tornado.httpclient


def getec(word):
    cli = tornado.httpclient.HTTPClient() #定义一个网页客户端类
    link = 'http://www.iciba.com/' # 主页网址
    link += word # 所查询单词的网址
    data = cli.fetch(link) # 抓取网页数据
    body = data.body.decode('utf8') # 转成utf-8编码
    soup = BeautifulSoup(body, 'html.parser') # 创建soup对象
    group = soup.find_all('li', class_='clearfix')
    # 寻找网页中的具有li样式的clearfix类
    shape = soup.find_all(class_='shape') # 寻找网页中的shape类
    long = len(group)
    d = {}
    means = []
    if long != 0: # 将词意和变形存到字典里
        if len(shape) != 0:
            for i in range(long-1):
                means.append((group[i]).text.replace('\n', ''))
            shape = (group[-1]).text.split()
            shape2 = []
            for i in range(1, len(shape), 2):
                shape2.append(shape[i] + shape[i+1])
            d['shape'] = shape2
        else:
            for i in range(long):
                means.append((group[i]).text.replace('\n', ''))
        d['means'] = means
    else:
        d['means'] = -1
    return d # 返回字典

if __name__ == '__main__':
    dic = getec('letter')
    print(dic)
