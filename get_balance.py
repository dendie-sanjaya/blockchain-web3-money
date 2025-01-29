from web3 import Web3

# Connect to Ganache
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Check if the connection is successful
if web3.is_connected():
    print("Connected to Ganache")
else:
    print("Failed to connect to Ganache")

# Replace this with the account address you want to check
account_address = "0x9064CE8365743E43399f6EEEB73E7fc0cc6e9127"

# Get the balance of the account
balance_wei = web3.eth.get_balance(account_address)
balance_ether = web3.from_wei(balance_wei, 'ether')

print(f"Balance of account {account_address}: {balance_ether} Ether")
