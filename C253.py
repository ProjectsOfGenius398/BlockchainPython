
# --------------253 Proj----------------
from web3 import Web3
import time

def wait():
	sleep(wait)
# Import time module here
 

ganache_url = 'http://127.0.0.1:7545'

web3_ganache_connection = Web3(Web3.HTTPProvider(ganache_url))

Alice_account = '0x16aA82894E5756e72AE90324C73cb7BD8cdf2339'
James_account = '0xCE0E55019739cf04cc8ADd780B84F5DF758daE92'
Ryan_account  = '0xe137F9F23C53B4A4bD76e06D2842061e0D41B810'


nonce1 = web3_ganache_connection.eth.getTransactionCount(Alice_account)

transaction_data1 = {
    'nonce':nonce1,
    'to':James_account,
    'value':web3_ganache_connection.toWei(50, 'ether'),
    'gas':21000,
    'gasPrice':web3_ganache_connection.toWei(50,'gwei')
}

private_key1 = '0x6e9b0edf2fd2e31c7dc1b33a3a1f84d5024708754c4b63439920c50d7e4b42d2'


singed_transaction1 = web3_ganache_connection.eth.account.signTransaction(transaction_data1,private_key1)
transaction_hash1 = web3_ganache_connection.eth.sendRawTransaction(singed_transaction1.rawTransaction)

print(web3_ganache_connection.toHex(transaction_hash1))



# -----------------
" the print statement and" 
sleep(5)
# -----------------



nonce2 = web3_ganache_connection.eth.getTransactionCount("Add sender account variable here")

transaction_data2 = {
    'nonce':"nonce2",
    'to':Ryan_account,
    'value':web3_ganache_connection.toWei("70", 'ether'),
    'gas':21000,
    'gasPrice':web3_ganache_connection.toWei(40,'gwei')
}

private_key2 = '0x6e9b0edf2fd2e31c7dc1b33a3a1f84d5024708754c4b63439920c50d7e4b42d2'

singed_transaction2 = web3_ganache_connection.eth.account.signTransaction(transaction_data2,private_key2)
transaction_hash2 = web3_ganache_connection.eth.sendRawTransaction(singed_transaction2.rawTransaction)

print(web3_ganache_connection.toHex(transaction_hash2))