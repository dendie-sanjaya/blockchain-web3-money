from web3 import Web3

# Koneksi ke Ganache
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Periksa apakah koneksi berhasil
if web3.is_connected():
    print("Terhubung ke Ganache")
else:
    print("Gagal terhubung ke Ganache")

# Mendapatkan daftar akun
accounts = web3.eth.accounts
print("Daftar akun di Ganache:")
for account in accounts:
    print(account)
