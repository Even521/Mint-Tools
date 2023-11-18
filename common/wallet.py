import getpass
from eth_account import Account
from common import pbeWithMd5Des

def create_wallet():
    Account.enable_unaudited_hdwallet_features()
    account, mnemonic = Account.create_with_mnemonic()
    privateKey = account._key_obj
    publicKey = privateKey.public_key
    address = publicKey.to_checksum_address()
    print(str(mnemonic), str(privateKey), str(address))
    return str(mnemonic), str(privateKey), str(address)

def create_pwd_wallet():
    Account.enable_unaudited_hdwallet_features()
    account, mnemonic = Account.create_with_mnemonic()
    privateKey = account._key_obj
    publicKey = privateKey.public_key
    address = publicKey.to_checksum_address()
    pwd = getpass.getpass("请输入你的密码:")
    word = pbeWithMd5Des.encrypt_pbe_with_md5_and_des(pwd, str(mnemonic))
    privateKeyEnc = pbeWithMd5Des.encrypt_pbe_with_md5_and_des(pwd, str(privateKey))
    # addressEnc = pbeWithMd5Des.encrypt_pbe_with_md5_and_des(pwd, str(address))

    pwd2 = getpass.getpass("请确认你的密码:")
    if pwd2 == pwd:
        if pbeWithMd5Des.decrypt_pbe_with_md5_and_des(pwd2, word) == str(
                mnemonic) and pbeWithMd5Des.decrypt_pbe_with_md5_and_des(pwd2, privateKeyEnc) == str(privateKey):
            print(f'助记词：{word}\n私钥：{privateKeyEnc}\n钱包地址：{str(address)}')
            with open('resource/wallet.txt', 'w') as f:
                f.write(f'助记词：{word}\n私钥：{privateKeyEnc}\n钱包地址：{str(address)}')
        else:
            print("加密异常")
    else:
        print("两次输入密码不一致")

if __name__ == '__main__':
    create_pwd_wallet()
