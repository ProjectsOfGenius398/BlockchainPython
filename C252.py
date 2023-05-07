from web3 import Web3

ganache_url = 'http://127.0.0.1:7545'
web3_ganache_connection = Web3(Web3.HTTPProvider(ganache_url))

Alice_account = '0x40B437B6F0b3a3434ed6542cF8347f4C23C9D7B4'
James_account = '0x263df012E011C476A865946922a94a883841fE55'

nonce = web3_ganache_connection.eth.getTransactionCount(Alice_account)
transaction_data = {
    'nonce':nonce,
    'to':James_account,
    'value':web3_ganache_connection.toWei(1, 'ether'),
    'gas':21000,
    'gasPrice':web3_ganache_connection.toWei(50,'gwei')
}
private_key = '0xfac298b5e73b78331a4711ed3c7d8d237ce611b36e2ea3b8374355c9a1906ccc'
signed_transaction = web3_ganache_connection.eth.account.signTransaction(transaction_data,private_key)
transaction_hash = web3_ganache_connection.eth.sendRawTransaction(signed_transaction.rawTransaction)


print(web3_ganache_connection.toHex(transaction_hash))

