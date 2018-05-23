# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 17:00:48 2018

@author: dutch
"""
import random
# change or not
N = 3
change = False

Total = 1000000
count = 0
for i in range(Total):
    car = random.randint(1,N) # 有汽车的门
    first_choose = random.randint(1,N) # 首次选择
    # 打开N-2个没有汽车的门
    if (first_choose == car):
        lefted = car+1 #如果一开始就猜对了，则随便留一个
    else:#如果一开始猜错了
        lefted = random.randint(car,car+(N-3))
    if (change):
        last_choose = lefted
    else:
        last_choose = first_choose
    p = 1 if (last_choose==car) else 0
    count = count + p;
str = "换" if (change) else "不"
print("换不换?\t%s:\t正确率:%f\n",str, count/Total);

