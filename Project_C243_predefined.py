from web3 import Web3
from web3.middleware import geth_poa_middleware

url = 'https://mainnet.infura.io/v3/cded6e6690d04259b05137dd10b170c3'
web3 = Web3(Web3.HTTPProvider(url))

Block_data = web3.eth.getBlock(12964964)
print('Block_data:', Block_data)

print('Gas_Used:', Block_data['gasUsed'])
print('TotalDifficulty:', Block_data['difficulty'])
print('Transaction_data:', Block_data['transactions'])

Transaction = web3.eth.get_transaction('0x4121669c46c143d17eb2233c8cd73ef52125cb5f0e352bac13093a628f958890')
print('data:', Transaction)

transaction_fee = web.eth.fee_history('')