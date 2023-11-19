# Mint-Tools 是链上批量Mint工具

1. python 安装 ： https://mirror.xyz/arant.eth/oy7DqPbsd1ySahHkqAkA7aaoX0efyI91YrPEb282Hl4

2. 使用说明请参照：  https://mirror.xyz/arant.eth/LdzJmoLXp59YCGJSrcWHm0nTArX1uC4dkNHoPcegc2w
3. 启动命令：
```agsl
python main.py
```
4. 启动配置文件 .env
```agsl
#可配置的内容
#请求节点路径
rpc_url={"polygon":"https://1rpc.io/matic","bsc":"https://1rpc.io/bnb"}
#链的ID
chain_id={"polygon":137,"bsc":56}



#需要配置的内容
#延迟时间（s）
delay = 0
#mint数量，如果值为空则为无限数量
num =
#链
chainName = "polygon"
#参数
data = {"p":"oft-20","op":"mint","tick":"ofts","amt":"1000"}
#钱包地址
account_address = '钱包地址'
#加密后的私钥
account_private_key = '加密后的私钥'
```
