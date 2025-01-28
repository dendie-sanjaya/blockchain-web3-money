from web3 import Web3

# Koneksi ke Ganache
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Periksa apakah koneksi berhasil
if web3.is_connected():
    print("Terhubung ke Ganache")
else:
    print("Gagal terhubung ke Ganache")

# Private key dari akun Ganache - sumber pengambil saldo
private_key = "0x5471e24d353e7abfe3b53fe0798cf26044f21b82083b93c7bef1c7bdcf7474e7"

# Dapatkan alamat akun dari private key
account = web3.eth.account.from_key(private_key)
account_address = account.address
print(f"Alamat akun Sumber: {account_address}")

# Periksa saldo akun
balance_wei = web3.eth.get_balance(account_address)
balance_ether = web3.from_wei(balance_wei, 'ether')
print(f"Saldo akun sumber {account_address}: {balance_ether} Ether")

# Contoh untuk membuat dan menandatangani transaksi - tujuan transfer
transaction = {
    'to': '0x22a443ee594F5fAE4DaE6613c7a38F7677102E41',  # Ganti dengan alamat penerima
    'value': web3.to_wei(1, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.to_wei('10000', 'gwei'),
    'nonce': web3.eth.get_transaction_count(account_address),
    'chainId': 1337  # ID rantai untuk Ganache
}
print(f"Jumlah Transfer: 10000 wei")


# Tanda tangani transaksi
signed_txn = web3.eth.account.sign_transaction(transaction, private_key)
tx_hash = web3.eth.send_raw_transaction(signed_txn.raw_transaction)
print(f"Transaksi hash: {web3.to_hex(tx_hash)}")


# Periksa saldo akun setelah perubah
balance_wei = web3.eth.get_balance(account_address)
balance_ether = web3.from_wei(balance_wei, 'ether')
print(f"Saldo akun sumber {account_address}: {balance_ether} Ether")


# Periksa saldo akun setelah perubah
balance_wei = web3.eth.get_balance('0x22a443ee594F5fAE4DaE6613c7a38F7677102E41')
balance_ether = web3.from_wei(balance_wei, 'ether')
print(f"Saldo akun tujuan {account_address}: {balance_ether} Ether")
