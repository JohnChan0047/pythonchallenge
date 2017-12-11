# -*- coding:utf-8 -*- 
__author__ = 'John 2017/12/10 22:26'

import requests
import re


next_code = '12345'
# next_code = '{0}'.format(int(16044/2))
code = ''
while next_code:
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+next_code
    response = requests.get(url)
    code = re.findall(r'.html$', response.text)
    if code:
        break
    code = re.findall(r'\d+$', response.text)
    if code:
        next_code = code[0]
    else:
        next_code = str(int(next_code/2))

url = 'http://www.pythonchallenge.com/pc/def/'+code[0]+'.html'

