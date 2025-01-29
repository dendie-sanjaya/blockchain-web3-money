from web3 import Web3

# Koneksi ke Ganache
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Periksa apakah koneksi berhasil
if web3.is_connected():
    print("Terhubung ke Ganache")
else:
    print("Gagal terhubung ke Ganache")

# Membuat akun baru
new_account = web3.eth.account.create()
new_address = new_account.address
new_private_key = new_account._private_key.hex()

print(f"Alamat baru: {new_address}")
print(f"Private key baru: {new_private_key}")

# Alamat akun yang digunakan untuk mengirim ETH (ganti dengan alamat yang sesuai)
sender_address = "0x22a443ee594F5fAE4DaE6613c7a38F7677102E41"
sender_private_key = "0x5096ee25d22eb8a62da464943bbbc19d8c0f2f4621c1d1f534d74f63fbb4ede1"

# Membuat transaksi untuk mengirim 1 ETH ke akun baru
transaction = {
    'to': new_address,
    'value': web3.to_wei(1, 'ether'),
    'gas': 21000,  # Gas limit standar untuk transaksi Ether
    'gasPrice': web3.to_wei('50', 'gwei'),  # Gas price yang wajar
    'nonce': web3.eth.get_transaction_count(sender_address),
    'chainId': 1337  # ID rantai untuk Ganache
}

# Tanda tangani transaksi
signed_txn = web3.eth.account.sign_transaction(transaction, sender_private_key)
tx_hash = web3.eth.send_raw_transaction(signed_txn.raw_transaction)
print(f"Transaksi hash: {web3.to_hex(tx_hash)}")

# Menunggu transaksi dikonfirmasi
web3.eth.wait_for_transaction_receipt(tx_hash)

# Periksa saldo akun baru
balance_wei = web3.eth.get_balance(new_address)
balance_ether = web3.from_wei(balance_wei, 'ether')
print(f"Saldo akun baru {new_address}: {balance_ether} Ether")

# Mendapatkan daftar semua akun termasuk akun baru
accounts = web3.eth.accounts + [new_address]

print("\nDaftar akun di Ganache (termasuk akun baru):")
for account in accounts:
    print(account)
