# -*- coding:utf-8 -*- 
__author__ = 'John 2017/12/10 21:44'

# 查看网页源码
from collections import Counter


with open('2.txt', 'r') as f:
    content = f.read()
    t = Counter(content).most_common()
    print(t)