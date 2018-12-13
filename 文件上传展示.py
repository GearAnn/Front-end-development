#!/usr/bin/python
# coding: utf-8 

"""
@version: Python3
@author: Ann 
@contact: 494792590@qq.com 
@software: Pycharm
@file: 文件上传展示.py
@time: 2018/11/4 0004 上午 3:02
"""

"""
通过html的表单上传文件：
<form>
    <input type='file'>
</form>

现在需要把上传后的文件写入硬盘（代码如下）
"""


def xiaohu(req):

    print('file:', req.FIlES)         # 文件上传到服务端后，是以字典的形式出现
    for item in req.FIlES:            # 利用item函数从字典(req.FILES)中取出键值对
        obj = req.FIlES.get(item)     # obj是个上传的文件对象
        filename = obj.name           # 因为对象中有name属性，所以可以直接调用

        f = open(filename, 'w')       # 打开的时候，文件对象不能直接打开,所以filename去接收对象的name属性

        for line in obj.chunks:       # 利用chunks函数分段截取文件对象
            f.write(line)

        f.close()