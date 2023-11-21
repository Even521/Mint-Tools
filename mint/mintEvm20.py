import json
from web3 import Web3
from common import pbeWithMd5Des, loadEnv
import time


def interactWeb3(web3, chainId, chainName, adress, data, private_key, gas_limit, multiple):
    print(f'公链：{chainName}   钱包地址：{adress}')
    gas_price = web3.eth.gas_price
    print(f'当前gas价格:{gas_price / 1_000_000_000} gwei')
    currentGas = int(gas_price / 1_000_000_000)

    if gas_limit != '' and currentGas > int(gas_limit):
        return -1
    else:
        tx = {
            'nonce': web3.eth.get_transaction_count(adress),
            'chainId': chainId,
            'to': adress,
            'from': adress,
            'data': data,  # mint 16进制数据
            'gasPrice': int(gas_price * multiple),
            'value': Web3.to_wei(0, 'ether')
        }
        nonce = web3.eth.get_transaction_count(adress)
        tx['nonce'] = nonce
        gas = web3.eth.estimate_gas(tx)
        tx['gas'] = gas

        print(f"交易消耗代币数量：{(tx['gasPrice'] / 1_000_000_000 * tx['gas']) / 1_000_000_000}")
        signed_tx = web3.eth.account.sign_transaction(tx, private_key)
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(f'交易TX：{web3.to_hex(tx_hash)}')
        receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
        return receipt.status


def mint(pwd):
    delay, num, privateKey_env, adress, rpc, chainId, chainName, data, gas_limit, multiple = loadEnv.loadDate()
    private_key = pbeWithMd5Des.decrypt_pbe_with_md5_and_des(pwd, privateKey_env)
    web3 = Web3(Web3.HTTPProvider(rpc))
    print(f'是否链接成功：{web3.is_connected()}')
    print(f'资产余额：{Web3.from_wei(web3.eth.get_balance(adress), "ether")}')
    success = 0
    failed = 0
    if num != '':
        n = 0
        while n < int(num):
            try:
                receipt = interactWeb3(web3, chainId, chainName, adress, data, private_key, gas_limit, multiple)
                if receipt.status == 1:
                    success += 1
                    print("~~~Mint Success~~~")

                elif receipt == -1:
                    time.sleep(3)
                    print(F'~~~等待gas下降到{gas_limit}才铸造~~~')
                else:
                    continue
            except Exception as e:
                print("~~~Mint Failed~~~")
                if str(e) == 'insufficient funds':
                    print("{chainName} 余额不足！")
                else:
                    print(f'ERROR:{e}')
                failed += 1
            n += 1
            print(F'{success} Success,{failed} Failed!\n\n')
            time.sleep(delay)
    else:
        while True:
            try:
                receipt = interactWeb3(web3, chainId, chainName, adress, data, private_key, gas_limit, multiple)
                if receipt == 1:
                    print("~~~Mint Success~~~")
                    success += 1
                elif receipt == -1:
                    time.sleep(3)
                    print(F'~~~等待gas下降到{gas_limit}才铸造~~~')
                else:
                    continue
            except Exception as e:
                print("~~~Mint Failed~~~")
                if str(e) == 'insufficient funds for transfer':
                    print("{chainName} 余额不足！")
                else:
                    print(f'ERROR:{e}')
                failed += 1
            print(F'{success} Success,{failed} Failed!\n\n')
            time.sleep(delay)
    print(f'成功：{success}\n失败:{failed}')
