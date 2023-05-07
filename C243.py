from web3 import Web3
from web3.middleware import geth_poa_middleware

API_url = 'https://mainnet.infura.io/v3/ec5acb1175dc468c9f3ee9a84a02fe98'
web3=Web3(Web3.HTTPProvider(API_url))

Block_data = web3.eth.getBlock(12964964)
print('Block data:', Block_data)
print('Total difficulty:',Block_data['difficulty'])

print('gasUsed:',Block_data['transactions'])
transaction=web3.eth.get_transaction('ac968d095d8f150b51c1332ab7f94482912087b6b1cbc8e139fd40170aa61cc3')
print('data', transaction)