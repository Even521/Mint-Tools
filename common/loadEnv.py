#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：mint-tool 
@File    ：loadEnv.py
@Author  ：Richard
@License ：(C) Copyright 2021-2022, Richard.
@Date    ：2023/11/19 00:58 
@contact :richard.eth@foxmail.com
'''
import os, json
from common import transferStr
from dotenv import load_dotenv

load_dotenv('env/.env')


def loadDate():
    privateKey_env = os.environ.get('account_private_key')
    delay = int(os.environ.get('delay'))
    num = os.environ.get('num')
    adress = os.environ.get('account_address')
    chainName = os.environ.get('chain_name')
    rpc = json.loads(os.environ.get('rpc_url'))[chainName]
    chainId = json.loads(os.environ.get('chain_id'))[chainName]
    gas_limit = os.environ.get('gas_limit')
    multiple = float(os.environ.get('multiple'))

    data = os.environ.get('data')
    if data.startswith('0x'):
        print(f'data为十六进制内容：{data}')
    else:
        print(f'data为字符串内容：{data}')
        data = ''.join(str(data).split())
        data = 'data:,' + data
        print(f'原始铭文信息：{data}')
        data = transferStr.encodeHex(data)
        print(f'十六进制铭文信息：{data}')

    return delay, num, privateKey_env, adress, rpc, chainId, chainName, data, gas_limit, multiple
