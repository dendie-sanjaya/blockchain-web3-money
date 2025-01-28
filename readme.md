 Upgrade Python Package Manager 
 --------------------------------
 python.exe -m pip install --upgrade --user pip
 
 
 Install Package Libry Python web3
 ---------------------------------
 pip install web3


Penjelasan Web3
--------------------------------------------

Web3 adalah istilah yang digunakan untuk menggambarkan evolusi terbaru dari internet yang didasarkan pada teknologi blockchain. Tujuan utama dari Web3 adalah memberikan desentralisasi dan kontrol penuh kepada pengguna atas data dan identitas mereka, berbeda dengan model terpusat yang ada pada Web2 (internet saat ini yang kita gunakan).

Beberapa konsep utama Web3 meliputi:

Desentralisasi: Data dan aplikasi tidak lagi dikendalikan oleh server terpusat, melainkan didistribusikan melalui jaringan komputer (blockchain).

Smart Contracts: Program yang berjalan di blockchain dan dieksekusi secara otomatis ketika kondisi tertentu terpenuhi. Smart contracts memungkinkan terjadinya transaksi tanpa perantara.

Cryptocurrency: Mata uang digital yang digunakan untuk transaksi di jaringan blockchain. Contoh populer termasuk Bitcoin dan Ethereum.

Identity and Data Ownership: Pengguna memiliki kontrol penuh atas data dan identitas mereka tanpa campur tangan pihak ketiga.

Interoperabilitas: Kemampuan aplikasi dan layanan dari berbagai blockchain untuk bekerja sama dan berbagi data



Install Ganache
-----------------

https://archive.trufflesuite.com/ganache/



Dalam jaringan Ethereum publik, setiap transaksi baru ditambahkan ke blok baru, dan blok tersebut ditambahkan ke blockchain. Proses ini terjadi di seluruh node dalam jaringan yang terdistribusi. Artinya, setiap node dalam jaringan Ethereum memiliki salinan lengkap dari seluruh blockchain, termasuk semua transaksi yang pernah terjadi.

Setiap kali transaksi baru dibuat dan dikonfirmasi, transaksi tersebut ditambahkan ke blok terbaru. Setelah blok tersebut berhasil ditambangkan dan ditambahkan ke blockchain, blok ini akan disebarkan ke semua node dalam jaringan. Semua node memperbarui salinan blockchain mereka untuk memasukkan blok baru ini.

Berikut adalah proses umum bagaimana transaksi ditambahkan ke blockchain Ethereum:

Transaksi dibuat: Transaksi baru dibuat dan disiarkan ke jaringan.

Transaksi disebarkan: Transaksi disebarkan ke semua node dalam jaringan Ethereum.

Transaksi dikumpulkan: Transaksi dikumpulkan oleh para penambang dan dimasukkan ke dalam blok baru.

Blok ditambangkan: Penambang mencoba untuk menyelesaikan masalah matematika (proof-of-work) untuk menambang blok baru.

Blok ditambahkan ke blockchain: Setelah blok berhasil ditambang, blok tersebut ditambahkan ke blockchain dan disebarkan ke semua node dalam jaringan.

Node memperbarui blockchain: Semua node memperbarui salinan blockchain mereka untuk memasukkan blok baru ini.

Jadi, setiap transaksi baru menambah satu entri dalam blok baru dan didistribusikan ke seluruh node dalam jaringan yang terdistribusi. Ini memastikan keamanan dan desentralisasi jaringan Ethereum.




Untuk membuat server blockchain on-premises, Anda dapat menggunakan beberapa framework yang populer dan mendukung desentralisasi serta keamanan. Berikut adalah beberapa framework yang bisa Anda pertimbangkan:

Hyperledger Fabric:

Hyperledger Fabric adalah platform blockchain yang dirancang untuk bisnis. Ini memungkinkan Anda untuk membuat jaringan permissioned (dengan izin) yang dapat diinstal di lingkungan on-premises2.

Hyperledger Fabric mendukung modulitas dan dapat diintegrasikan dengan sistem bisnis yang ada.

Ethereum:

Ethereum juga dapat diinstal di lingkungan on-premises. Anda dapat menggunakan Ethereum untuk membuat aplikasi blockchain dan menjalankan smart contracts.

Ethereum memerlukan node yang lebih besar untuk menyimpan dan memproses semua transaksi dalam jaringan.

IBM Blockchain Platform:

IBM Blockchain Platform mendukung instalasi di lingkungan on-premises. Anda dapat menggunakan platform ini untuk membangun dan mengelola jaringan blockchain di dalam perangkat keras Anda2.

Platform ini mendukung Kubernetes dan OpenShift untuk pengelolaan cluster blockchain.

SettleMint:

SettleMint menawarkan solusi on-premises untuk pengembangan blockchain. Anda dapat menginstal dan menjalankan aplikasi blockchain di infrastruktur Anda sendiri3.

SettleMint mendukung berbagai metode instalasi, termasuk air-gapped (tidak terhubung ke internet) dan Bring Your Own Cloud (BYOC)

