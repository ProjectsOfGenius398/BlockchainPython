from web3 import Web3

infura_url='https://mainnet.infura.io/v3/9cd07f2dcb5248cba4b2c35638dcf886'

web3_infura_connection=Web3(Web3.HTTPProvider(infura_url))
account1='0x9333e6A4A354029b6441942CA2c0540707ecfeC8'
account2='0xA9fE0AE4D1f287a696601F601Ce4936ceb6D2A5E'

private_key='0x5934e40b07f1e2450bdb8d37c2868f3d5bae94a261f4377fac976eedb2685999'

nonce=web3_infura_connection.eth.getTransactionCount(account1)
transaction_data={
	'nonce':nonce,
	'to':account2,
	'value':web3_infura_connection.toWei(0.0001,'ether'),
	'gas':21000,
	'gasPrice':web3_infura_connection.toWei(30,'gwei')
}

signed_transaction=web3_infura_connection.eth.account.signTransaction(transaction_data,private_key)
transaction_hash=web3_infura_connection.eth.sendRawTransaction(signed_transaction.rawTransaction)

print(web3_infura_connection.toHex(transaction_hash))