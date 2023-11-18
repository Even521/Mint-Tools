#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：mint-tool-master 
@File    ：transferStr.py
@Author  ：Richard
@License ：(C) Copyright 2021-2022, Richard.
@Date    ：2023/11/18 15:02 
@contact :richard.eth@foxmail.com
'''
def  decodeHex(str):
    return bytes.fromhex(str[2:]).decode('utf-8')

def encodeHex(str):
    return '0x'+str.encode('utf-8').hex()

def comString(str1, str2):
    if str1 == str2:
        print('T')
    else:
        print('F')