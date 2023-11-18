import json
from web3 import Web3
from dotenv import load_dotenv
import os,getpass
load_dotenv()
import pbeWithMd5Des
import transferStr
import time

def mint(pwd=None):
    envKey=os.environ.get('account_private_key')
    delay = int(os.environ.get('delay'))
    num = os.environ.get('num')
    private_key = pbeWithMd5Des.decrypt_pbe_with_md5_and_des(pwd,envKey)
    adress = os.environ.get('account_address')
    data = json.loads(os.environ.get('data'))
    chainName = os.environ.get('chainName')
    if chainName == 'bsc':
        rpc = json.loads(os.environ.get('rpc_url'))['bsc']
        chain = json.loads(os.environ.get('chain_id'))['bsc']
    elif chainName == 'polygon':
        rpc = json.loads(os.environ.get('rpc_url'))['polygon']
        chain = json.loads(os.environ.get('chain_id'))['polygon']
    print(f'RPC:{rpc}\nChainId:{chain}')
    data = ''.join(str(data).split())
    data = 'data:,' + data
    print(f'原始铭文信息：{data}')
    data = transferStr.encodeHex(data)
    print(f'十六进制铭文信息：{data}')
    web3 = Web3(Web3.HTTPProvider(rpc))
    print(f'是否链接成功：{web3.is_connected()}')
    print(f'资产余额：{Web3.from_wei(web3.eth.get_balance(adress),"ether")}')
    c = 0
    success = 0
    failed = 0
    if num != '':
        n = 0
        while n < int(num):
            try:
                nonce = web3.eth.get_transaction_count(adress)
                tx = {
                    'nonce': nonce,
                    'chainId': chain,
                    'to': adress,
                    'from': adress,
                    'data': data,  # mint 16进制数据
                    'gasPrice': web3.eth.gas_price,
                    'value': Web3.to_wei(0, 'ether')
                }
                gas = web3.eth.estimate_gas(tx)
                tx['gas'] = gas
                print(f'交易参数：{tx}')
                signed_tx = web3.eth.account.sign_transaction(tx, private_key)
                tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
                print(f'交易TX：{web3.to_hex(tx_hash)}')
                receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
                if receipt.status == 1:
                    c = c + 1
                    print("%s Mint Success!" % c)
                    success += 1
                    # continue
                else:
                    continue
            except Exception as e:
                print(f'ERROR:{e}')
                failed += 1
            n += 1
            time.sleep(delay)
    else:
        while True:
            try:
                nonce = web3.eth.get_transaction_count(adress)
                tx = {
                    'nonce': nonce,
                    'chainId': chain,
                    'to': adress,
                    'from': adress,
                    'data': data,  # mint 16进制数据
                    'gasPrice': web3.eth.gas_price,
                    'value': Web3.to_wei(0, 'ether')
                }
                gas = web3.eth.estimate_gas(tx)
                tx['gas'] = gas
                print(tx)
                signed_tx = web3.eth.account.sign_transaction(tx, private_key)
                tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
                print(web3.to_hex(tx_hash))
                receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
                if receipt.status == 1:
                    c = c + 1
                    print("%s Mint Success!" % c)
                    success += 1
                    # continue
                else:
                    continue
            except Exception as e:
                print(f'ERROR:{e}')
                failed += 1
            time.sleep(delay)
    print(f'成功：{success}\n失败:{failed}')

