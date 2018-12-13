#!/usr/bin/python
# coding: utf-8 

"""
@version: Python3
@author: Ann 
@contact: 494792590@qq.com 
@software: Pycharm
@file: 客户端.py
@time: 2018/11/2 0002 上午 4:35
"""

"""
本节内容：自己写一个小的网页，网页内容放在HTTP文本里面，用谷歌流浪器打开
"""


import socket


def main():
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.bind(('127.0.0.1', 8089))
    sk.listen()

    while True:
        conn, addr = sk.accept()
        buf = conn.recv(1024)
        print(buf.decode('utf8'))

        with open('hello.html', 'rb') as f:
            data = f.read()

        conn.sendall(data)

        conn.close()


if __name__ == '__main__':
    main()





