import json
from web3 import Web3
from common import  pbeWithMd5Des,loadEnv
import time

def interactWeb3(web3,chainId,adress,data,private_key):
    tx = {
        'nonce': web3.eth.get_transaction_count(adress),
        'chainId': chainId,
        'to': adress,
        'from': adress,
        'data': data,  # mint 16进制数据
        'gasPrice': web3.eth.gas_price,
        'value': Web3.to_wei(0, 'ether')
    }
    nonce = web3.eth.get_transaction_count(adress)
    tx['nonce'] = nonce
    gas = web3.eth.estimate_gas(tx)
    tx['gas'] = gas
    print(f'交易参数：{tx}')
    signed_tx = web3.eth.account.sign_transaction(tx, private_key)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print(f'交易TX：{web3.to_hex(tx_hash)}')
    receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

    return receipt

def mint(pwd):
    delay, num, privateKey_env, adress, rpc, chainId,data = loadEnv.loadDate()
    private_key = pbeWithMd5Des.decrypt_pbe_with_md5_and_des(pwd, privateKey_env)
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
                receipt = interactWeb3(web3, chainId, adress, data, private_key)
                if receipt.status == 1:
                    c = c + 1
                    print("%s Mint Success!" % c)
                    success += 1
                    # continue
                else:
                    continue
            except Exception as e:
                if str(e) == 'insufficient funds':
                    print("余额不足！")
                else:
                    print(f'ERROR:{e}')
                failed += 1
            n += 1
            time.sleep(delay)
    else:
        while True:
            try:
                receipt = interactWeb3(web3, chainId, adress, data, private_key)
                if receipt.status == 1:
                    c = c + 1
                    print("%s Mint Success!" % c)
                    success += 1
                    # continue
                else:
                    continue
            except Exception as e:
                if str(e) == 'insufficient funds for transfer':
                    print("余额不足！")
                else:
                    print(f'ERROR:{e}')
                failed += 1
            time.sleep(delay)
    print(f'成功：{success}\n失败:{failed}')

