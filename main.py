#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：mint-tool-master 
@File    ：main.py
@Author  ：Richard
@License ：(C) Copyright 2021-2022, Richard.
@Date    ：2023/11/18 22:31 
@contact :richard.eth@foxmail.com
'''
from common import wallet, pbeWithMd5Des
from mint import mintEvm20
import getpass

def main():
    print("操作说明：\n1.创建钱包\n2.加密私钥/助记词\n3.解密私钥/助记词\n4.Mint EVM铭文\n输入'h'或者'帮助'查看菜单详情")
    while True:
        action = input("请输入你的操作：")
        try:
            if action == 'h' or action == '帮助':
                print(
                    "操作说明：\n1.创建钱包\n2.加密私钥/助记词\n3.解密私钥/助记词\n4.Mint EVM铭文\n输入'h'或者'帮助'查看菜单详情")
            elif int(action) == 1:
                wallet.create_pwd_wallet()
            elif int(action) == 2:
                password = getpass.getpass("输入密码：")
                plaintext = input("输入私钥/助记词：")
                # Encrypt
                encrypted_text = pbeWithMd5Des.encrypt_pbe_with_md5_and_des(password, plaintext)
                print(f"Encrypted Text:{encrypted_text}")
            elif int(action) == 3:
                password = getpass.getpass("输入密码：")
                plaintext = input("输入私钥/助记词：")
                #Decrypt
                decrypted_text = pbeWithMd5Des.decrypt_pbe_with_md5_and_des(password, plaintext)
                print(f"Decrypted Text:{decrypted_text}",)
            elif int(action) == 4:
                pwd = getpass.getpass("请输入你的密码:")
                mintEvm20.mint(pwd)
            else:
                print("请输入正确的指令！")
        except Exception as e:
            print(f'ERROR111:{e}')

if __name__ == '__main__':
    main()

