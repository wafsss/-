import privatekey
import Web3 import Web3
import usdt_abi


##############################
#private_key = 'xxxx'  防止私钥被看到

# fromAddress = Web3.toChecksumAddress(fromAddress)
# toAddress = Web3.toChecksumAddress(toAddress)

fromAddress = Web3.toChecksumAddress(0x42B83d07e3255db18aB2d5e8Fe164)
toAddress = Web3.toChecksumAddress(0x42B83d07e3255db18aB2d5e8Fe1)
gasPrice = 10          #单位为gwei
usdt = 100             #单位为usdt
##############################

usdt_num =  usdt * 10**6
v_gasPrice = Web3.toWei(gasPrice, 'gwei')

w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'))

#https://etherscan.io/address/0xdac17f958d2ee523a2206206994597c13d831ec7,获取solidity代码进入remix,获取abi合约+abi,用于test
USDT_address = 'Web3.toChecksumAddress('0xebc8cDAEbA0048a4CA86e9Cd5A2943f79650B89a')'
USDT_contract = w3.eth.contract(address=USDT_address, abi=usdt_abi.abi_usdt)


nonce = w3.eth.getTransactionCount(fromAddress)
print('nonce:',nonce)

gas = USDT_contract.functions.transfer(toAddress, usdt_num).estimateGas({'from': fromAddress})
print('gas:',gas)

transaction = USDT_contract.functions.transfer(toAddress, usdt_num).buildTransaction({
    'gas': gas,
    'gasPrice': v_gasPrice,
    'nonce': nonce,
})
print('transaction',transaction)

start = input("警告！请确认是否要进行转账操作，输入yes进行转账：")
print(start)

if start == 'yes':
    signed_txn = w3.eth.account.signTransaction(transaction, private_key=privatekey.private_key)
    print('signed_txn:',signed_txn)
    result = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
    print('result:',result)
    print('https://etherscan.io/tx/' + Web3.toHex(result))
else:
    print('取消转账操作！')




