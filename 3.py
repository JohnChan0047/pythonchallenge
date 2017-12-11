# -*- coding:utf-8 -*- 
__author__ = 'John 2017/12/10 21:59'
# 查看网页源码
import re

with open('3.txt', 'r') as f:
    content = f.read()
    content = content.replace('\n', '')
    chars = re.findall(r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', content)
    print(''.join(chars))