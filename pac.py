# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 17:01:19 2018

@author: dutch
"""

import urllib.request
import re
import time
import random

baseUrl="http://jwxk.ucas.ac.cn/course/coursetime/"
lst = list(range(142200, 142700))
# random.shuffle(lst) #打乱顺序
for index in lst:
    indexUrl = baseUrl + str(index)
    
    html =urllib.request.urlopen(indexUrl).read()
    html=html.decode('utf8')
    
    class_name=re.findall('<p>课程名称：(.*?)</p>.*?<p>(.*?)：</p>',html,re.S)
    print("%s：" %str(index))
    print(class_name)
    with open('class.txt', 'a') as f:
        f.write("%s：" %str(index))
        f.write(str(class_name))
        f.write("\n")
    
    time.sleep(random.random()/2+0.01)


