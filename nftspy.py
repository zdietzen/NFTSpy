import requests
import time
import json
import web3
from web3 import Web3
# from web3.auto.infura import w3

from web3 import Web3
from web3 import contract
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/<PROJECT_ID_HERE>'))


api_key = '<API_KEY_HERE>'
wallet_address = '0x95abDa53Bc5E9fBBDce34603614018d32CED219e' #cuban's
# contract_address = '0xc5a49b4cbe004b6fd55b30ba1de6ac360ff9765d'


#get the balance on the account in ETH
# url = 'https://api.etherscan.io/api' \
#         '?module=account' \
#         '&action=balance'\
#         '&address={}' \
#         '&tag=latest'  \
#         '&apikey={}'.format(wallet_address,api_key)

# response = requests.get(url)
# print(response)
# print(response.json())

#Returns the Contract Application Binary Interface ( ABI ) of a verified smart contract
# url = 'https://api.etherscan.io/api' \
#         '?module=contract' \
#         '&action=getabi'\
#         '&address={}' \
#         '&apikey={}'.format(wallet_address,api_key)

# response = requests.get(url)
# print(response)
# print(response.json())

# #Returns the Contract Application Binary Interface ( ABI ) of a verified smart contract
# url = 'https://api.etherscan.io/api' \
#         '?module=transaction' \
#         '&action=getstatus'\
#         '&txhash=0x0a0ab14393a85831838c6c51deeae6584e8a520a0df7e6cfd28a294ad92911e8' \
#         '&apikey={}'.format(api_key)

# response = requests.get(url)
# print(response)
# print(response.json())


#Returns the list of transactions performed by an address, with optional pagination.
# offset_num=0
# url = 'https://api.etherscan.io/api' \
#         '?module=account' \
#         '&action=txlist'\
#         '&address={}' \
#         '&startblock=0' \
#         '&endblock=99999999' \
#         '&page=1' \
#         '&offset={}' \
#         '&sort=desc' \
#         '&apikey={}'.format(wallet_address,offset_num,api_key)

# response = requests.get(url)
# print(response)
# receiving_address = response.json()['result'][0]['to']
# trx_list = response.json()['result']

# num_of_trx = len(trx_list)
# # print(num_of_trx)
# trx_num = 0

# while trx_num < num_of_trx:

#     # timestamp = int(trx_list[trx_num]['timeStamp'])
#     # time_of_trx = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))
#     # print(time_of_trx)

#     trx_hash = trx_list[trx_num]['hash']
#     # print(receiving_address)
#     print(trx_hash)
        
#     quit()

#     trx_num += 1


#Returns the information about a transaction requested by transaction hash.
trx_hash = '0x0a0ab14393a85831838c6c51deeae6584e8a520a0df7e6cfd28a294ad92911e8'

# url = 'https://api.etherscan.io/api' \
#         '?module=proxy' \
#         '&action=eth_getTransactionByHash'\
#         '&txhash={}' \
#         '&apikey={}'.format(trx_hash,api_key)

# response = requests.get(url)
# print(response)
# trx_return = response.json()
# print(trx_return)


# # #Returns the Contract Application Binary Interface ( ABI ) of a verified smart contract
# url = 'https://api.etherscan.io/api' \
#         '?module=contract' \
#         '&action=getabi'\
#         '&address=0xdef171fe48cf0115b1d80b88dc8eab59176fee57' \
#         '&apikey={}'.format(api_key)

# # response = requests.get(url)
# # print(response)
# # print(response.json())


# Get transaction object
tx = w3.eth.get_transaction(trx_hash)

# Get ABI for smart contract NOTE: Use "to" address as smart contract 'interacted with'
abi_endpoint = 'https://api.etherscan.io/api?module=contract&action=getabi&address={}&apikey={}'.format(tx['to'],api_key)
abi = json.loads(requests.get(abi_endpoint).text)

# print(abi)

# print(abi['result'])

# Create Web3 contract object
# contract1 = w3.eth.contract(address=w3.toChecksumAddress('0xdef171fe48cf0115b1d80b88dc8eab59176fee57'), abi=abi['result'])
contract1 = w3.eth.contract(address=tx["to"], abi=abi["result"])

# print(contract1)

# Decode input data using Contract object's decode_function_input() method
# func_obj, func_params = contract1.decode_function_input(tx['input'])
func_obj, func_params = contract1.decode_function_input(tx["input"])

print("----")
print(func_obj)
print(func_params)




# print(int(trx_return['result']['input'],16))

# print(trx_return['result']['input'])

# print(web3.Web3.toText(trx_return['result']['input']))


# web3.eth.get_balance('0xd3CdA913deB6f67967B99D67aCDFa1712C293601')

# transaction = w3.eth.get_transaction('0x0a0ab14393a85831838c6c51deeae6584e8a520a0df7e6cfd28a294ad92911e8')

# print(type(transaction['input']))

# # contract.Contract.

# contract.Contract.abi.__init__.

# print(abi.decode_function_input(transaction['input']))

# print(contract.Contract.abi('0xa9cb55d05d3351dcd02dd5dc4614e764ce3e1d6e'))

# my_contract = w3.eth.contract('0x95abDa53Bc5E9fBBDce34603614018d32CED219e')
# print(my_contract.all_functions())
