from web3 import Web3

# Koneksi ke Ganache
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Alamat yang akan diperiksa
address_to_check = "0x22a443ee594F5fAE4DaE6613c7a38F7677102E41"

# Fungsi untuk mendapatkan riwayat transaksi untuk sebuah alamat
def get_transaction_history(address):
    transactions = []
    latest_block = web3.eth.block_number

    for block_number in range(latest_block + 1):
        block = web3.eth.get_block(block_number, full_transactions=True)
        for tx in block.transactions:
            if tx['from'] == address or tx['to'] == address:
                transactions.append({
                    'block': block_number,
                    'hash': tx['hash'].hex(),
                    'from': tx['from'],
                    'to': tx['to'],
                    'value': web3.from_wei(tx['value'], 'ether'),
                    'gas': tx['gas'],
                    'gasPrice': web3.from_wei(tx['gasPrice'], 'gwei')
                })
    
    return transactions

# Mendapatkan riwayat transaksi untuk alamat yang ditentukan
history = get_transaction_history(address_to_check)

# Menampilkan riwayat transaksi
if history:
    for tx in history:
        print(f"Block: {tx['block']}, Hash: {tx['hash']}, From: {tx['from']}, To: {tx['to']}, Value: {tx['value']} Ether, Gas: {tx['gas']}, Gas Price: {tx['gasPrice']} Gwei")
else:
    print(f"Tidak ada transaksi ditemukan untuk alamat {address_to_check}")
