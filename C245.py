from web3 import Web3
import json
import requests

infura_url='https://mainnet.infura.io/v3/ec5acb1175dc468c9f3ee9a84a02fe98'
web3=Web3(Web3.HTTPProvider(infura_url))

req_ethgas_data=requests.get('https://ethgasstation.info/json/ethgasAPI.json')
trans_info=json.loads(req_ethgas_data.content)

print('safeLow', trans_info['safeLow'])
print('average', trans_info['average'])
print('fast',trans_info['fast'])
print('fastest',trans_info['fastest'])
print('Block nubmer:', trans_info['blockNum'])

gas_Price=web3.eth.gasPrice
print('Gas: ', gas_Price/10**9)