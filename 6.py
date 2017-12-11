# -*- coding:utf-8 -*- 
__author__ = 'John 2017/12/11 10:09'
import zipfile
import re


z = zipfile.ZipFile('channel.zip', 'r')
next_code = '90052'
comments = []
while True:
    filename = next_code + '.txt'
    comments.append(z.getinfo(filename).comment.decode('utf-8'))
    g = z.read(z.getinfo(filename)).decode('utf-8')
    m = re.match('Next nothing is (\d+)', g)
    if m:
        next_code = m.group(1)
    else:
        break

print(''.join(comments))

"""
****************************************************************
****************************************************************
**                                                            **
**   OO    OO    XX      YYYY    GG    GG  EEEEEE NN      NN  **
**   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE  NN    NN   **
**   OO    OO XXX  XXX YYY   YY  GG GG     EE       NN  NN    **
**   OOOOOOOO XX    XX YY        GGG       EEEEE     NNNN     **
**   OOOOOOOO XX    XX YY        GGG       EEEEE      NN      **
**   OO    OO XXX  XXX YYY   YY  GG GG     EE         NN      **
**   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE     NN      **
**   OO    OO    XX      YYYY    GG    GG  EEEEEE     NN      **
**                                                            **
****************************************************************
 **************************************************************
 oxygen
"""