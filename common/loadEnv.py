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
    data = json.loads(os.environ.get('data'))
    chainName = os.environ.get('chain_name')
    if chainName == 'bsc':
        rpc = json.loads(os.environ.get('rpc_url'))['bsc']
        chainId = json.loads(os.environ.get('chain_id'))['bsc']
    elif chainName == 'polygon':
        rpc = json.loads(os.environ.get('rpc_url'))['polygon']
        chainId = json.loads(os.environ.get('chain_id'))['polygon']
    elif chainName == 'okb':
        rpc = json.loads(os.environ.get('rpc_url'))['okb']
        chainId = json.loads(os.environ.get('chain_id'))['okb']
    elif chainName == 'avax':
        rpc = json.loads(os.environ.get('rpc_url'))['avax']
        chainId = json.loads(os.environ.get('chain_id'))['avax']
    print(f'RPC:{rpc}\nChainId:{chainId}')
    data = ''.join(str(data).split())
    data = 'data:,' + data
    print(f'原始铭文信息：{data}')
    data = transferStr.encodeHex(data)
    print(f'十六进制铭文信息：{data}')
    return delay, num, privateKey_env, adress, rpc, chainId, data
