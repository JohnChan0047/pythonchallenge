# -*- coding:utf-8 -*- 
__author__ = 'John 2017/12/10 16:54'

string1 = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'+'\''+'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'


def func(string):
    chr_list = []
    for j in (ord(i) for i in string):
        if j < 121:
            j = j + 2
        else:
            j = j + 2 - 26
        chr_list.append(j)

    string2 = ''

    for code in chr_list:
        string2 = string2 + chr(code)

    return string2


print(func('map'))

