from web3 import Web3

# Menghubungkan ke blockchain lokal yang dijalankan oleh Ganache
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Memeriksa koneksi
if web3.is_connected():
    print("Koneksi berhasil!")
else:
    print("Koneksi gagal!")
