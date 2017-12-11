# -*- coding:utf-8 -*- 
__author__ = 'John 2017/12/11 11:34'
from PIL import Image


target = ''
image = Image.open('oxygen.png')
for i in range(0, 607, 7):
    for x in chr(image.getpixel((i, 50))[0]):
        target += x
print(target)
print(''.join(chr(x) for x in [105, 110, 116, 101, 103, 114, 105, 116, 121]))

"""
smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]
integrity
"""