from web3 import Web3

ganache_url='http://127.0.0.1:7545'
web3_ganache_connection=Web3(Web3.HTTPProvider(ganache_url))

Alice='0x9333e6A4A354029b6441942CA2c0540707ecfeC8'
James='0xA9fE0AE4D1f287a696601F601Ce4936ceb6D2A5E'

nonce=web3_ganache_connection.eth.getTransactionCount(Alice)
transactionData={
	'nonce': nonce,
	'to':James,
	'value':web3_ganache_connection.toWei(20, 'ether'),
	'gas':21000,
	'gasPrice':web3_ganache_connection.toWei(0.000525,'gwei')
}
privateKey='0x5934e40b07f1e2450bdb8d37c2868f3d5bae94a261f4377fac976eedb2685999'
signedTransaction=web3_ganache_connection.eth.account.signTransaction(transactionData, privateKey)
transactionHash=web3_ganache_connection.eth.sendRawTransaction(signedTransaction.rawTransaction)

print(web3_ganache_connection.toHex(transactionHash))