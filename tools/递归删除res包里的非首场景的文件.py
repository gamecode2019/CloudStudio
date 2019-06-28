# ! /usr/bin/python
# -- coding: utf-8 --
import re
import os
import sys
filterFiles = ['81e988e8-8c0b-4694-84ef-3e65a2b6bad5.13733.json',
'02fce8bbb.aba2e.json',
'071642ea3.25340.json',
'01842d971.2d111.json',
'18eacc55d.e6c9c.png',
'ea3b2ce3-87bb-4674-b7a9-3f276163f45c.18db0.png',
'247fd773-6e3f-4b7a-b7d1-121ef7c011f3.eea0d.png',
'e71e5a55-afd2-480c-aa09-f6dbd28aa0dc.237e6.png',
'1da64b0ce.237f8.png',
'1e22c50a9.d242a.png'
]
def del_dir_tree(path):
    # ''' 递归删除目录及其子目录, 子文件'''
    if os.path.isfile(path):
        try:
            # os.remove(path)
            array = path.split('\\')
            fileName = array[len(array)-1]
            if fileName not in filterFiles:
                
                os.remove(path)
        except Exception, e:
            #pass
            print e
    elif os.path.isdir(path):
        for item in os.listdir(path):
            itempath = os.path.join(path, item)
            del_dir_tree(itempath)
    try:
        os.rmdir(path) # 删除空目录
        # print path
    except Exception, e:
        pass
        # print e

if __name__ == '__main__':
    dirname = 'D:\\SVN\\fighter\\Project\\release_wx\\wechatgame\\res'
    del_dir_tree(dirname)