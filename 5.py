# -*- coding:utf-8 -*- 
__author__ = 'John 2017/12/11 0:08'
import pickle

with open('banner.p', 'rb') as f:
    banner = pickle.load(f)
    for linelist in banner:
        print("".join(ch * count for ch, count in linelist))



