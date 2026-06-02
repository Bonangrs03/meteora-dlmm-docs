# Chapter 11: Gimana DLMM Beda

---

## Bukan Sekadar Kloningan Uniswap

Uniswap V3 mempelopori concentrated liquidity di Ethereum. Revolusioner. Tapi Meteora DLMM bukan kopian — ini desain yang fundamentally beda, dibangun dari nol buat Solana.

Ini yang bikin mereka beda — dan kenapa ini penting buat lo sebagai LP.

## Bin vs Tick: Diskrit vs Kontinu

| | Uniswap V3 | Meteora DLMM |
|---|---|---|
| **Representasi harga** | "Tick" kontinu — gradien halus | Bin diskrit — titik harga spesifik |
| **Di dalam satu unit** | Harga berubah setiap trade (constant product) | Harga tetap sampai bin terkuras (constant sum) |
| **Slippage** | Setiap trade menggerakkan harga | Zero slippage dalam satu bin |
| **Mental model** | "Gue nyediain likuiditas antara X dan Y" | "Gue naruh likuiditas di anak tangga harga tertentu" |

Perbedaan ini kedengeran subtle tapi punya konsekuensi nyata. Di Uniswap V3, bahkan trade kecil sekalipun menggerakkan harga sedikit. Di DLMM, trade kecil dieksekusi di harga bin yang persis tanpa impact. Harga cuma bergerak pas bin dikosongkan — kayak nguras ember sebelum pindah ke ember berikutnya.

Buat trader, ini artinya eksekusi lebih baik di order kecil. Buat LP, ini artinya modal lo dikerahkan dengan lebih predictable.

## Dynamic Fee vs Static Fee

| | Uniswap V3 | Meteora DLMM |
|---|---|---|
| **Struktur fee** | Tier fee tetap (0.05%, 0.3%, 1%) | Base fee + variable fee |
| **Adaptasi market** | Nggak ada — tier fee dipilih sekali doang | Fee naik pas volatilitas, turun pas tenang |
| **Perlindungan LP** | Fee sama terlepas kondisi market | Fee lebih tinggi pas LP lagi lebih berisiko |

Ini mungkin inovasi DLMM yang paling penting. Fee tetap Uniswap V3 artinya lo dapet persentase yang sama entah market lagi tenang atau kacau — padahal lo ngambil risiko jauh lebih banyak pas kacau. DLMM ngompensasi lo lebih banyak pas lo ngambil lebih banyak risiko.

## Limit Order Bawaan

Ini yang Uniswap V3 nggak punya: **limit order built-in ke dalam posisi LP.**

Di DLMM, kalo lo deposit likuiditas di satu bin di atas harga saat ini (semua quote token), posisi itu secara alami bertindak sebagai limit sell order. Kalo harga nyampe bin itu, quote token lo berubah jadi base token — persis kayak yang dilakukan limit order.

Sama juga, satu bin di bawah harga saat ini (semua base token) bertindak sebagai limit buy order.

| Fitur DLMM | Padanan di Keuangan Tradisional |
|------------|--------------------------------|
| Satu bin di atas harga, semua USDC | Limit sell order |
| Satu bin di bawah harga, semua SOL | Limit buy order |
| Bin tersebar di sekitar harga | Posisi LP (dapet fee) |

Ini artinya DLMM menggabungin dua hal yang terpisah di kebanyakan protokol DeFi: LPing dan limit order. Posisi LP lo *adalah* strategi trading lo.

## Posisi yang Bisa Di-resize

Di Uniswap V3, posisi likuiditas lo adalah NFT (non-fungible token). Lo nggak bisa gampang nambah atau ngurangin — lo tutup dan buka yang baru.

Di DLMM, posisi itu **bisa di-resize.** Lo bisa:

- Nambah lebih banyak likuiditas ke posisi yang udah ada
- Narik sebagian likuiditas lo tanpa nutup
- Nyetel ulang rentang bin lo tanpa mulai dari awal
- Support sampai 1.400 bin dalam satu posisi

Ini penting buat manajemen aktif. Kalo lo pengen DCA (dollar-cost average) masuk ke posisi secara bertahap, atau keluar bertahap, DLMM support secara native.

## Solana-Native: Account vs NFT

| | Uniswap V3 (Ethereum) | Meteora DLMM (Solana) |
|---|---|---|
| **Representasi posisi** | NFT ERC-721 | Solana account (PositionV2) |
| **Biaya bikin posisi** | $30–100+ gas | ~$0.0002 |
| **Biaya modifikasi posisi** | $20–80+ gas | ~$0.0002 |
| **Manajemen aktif praktis** | Cuma buat whale ($10K+) | Bisa buat siapa aja ($20+) |

Ini keunggulan Solana yang kita bahas di Chapter 8, dibuat konkret. Desain protokol yang sama di Ethereum bakal nggak usable buat LP retail. Di Solana, accessible.

## Liquidity Mining: Reward Bawaan

Pool DLMM bisa punya sampai dua reward token yang dibagiin ke LP, di atas trading fee. Ini built-in ke protokol, bukan ditempel belakangan.

Contohnya, proyek token baru mungkin bikin pool DLMM dan nambahin token mereka sebagai reward buat insentif LP awal. Lo dapet trading fee DAN reward token.

## Tradeoff: Program Closed-Source

Ada satu hal penting yang perlu lo tau: program inti DLMM di Solana (`lb_clmm`) itu **nggak open source.** SDK, dokumentasi, tools integrasi semuanya open — tapi program on-chain-nya sendiri closed.

| Yang Open | Yang Closed |
|-----------|-------------|
| TypeScript SDK (`@meteora-ag/dlmm`) | Program on-chain inti |
| Dokumentasi (docs.meteora.ag) | |
| DAMM v2 program (protokol terkait) | |
| Data API | |

Ini nggak ngaruh ke lo sebagai LP — lo interaksi lewat interface yang udah diaudit dan didokumentasikan dengan baik. Tapi worth knowing. Tim maintain ini sebagai pilihan strategis, bukan kurang transparansi (SDK dan docs-nya komprehensif).

## Rangkuman: DLMM vs Uniswap V3 Sekilas

| Dimensi | Uniswap V3 | Meteora DLMM |
|---------|-----------|--------------|
| Blockchain | Ethereum (dan L2) | Solana |
| Model harga | Tick kontinu | Bin diskrit |
| Model fee | Tier tetap | Dinamis (base + variable) |
| Limit order | Nggak | Iya, native |
| Manajemen posisi | Berbasis NFT, susah dimodifikasi | Berbasis account, bisa di-resize |
| Biaya transaksi | Tinggi ($5–100) | Hampir nol (~$0.0002) |
| Manajemen aktif | Wilayah whale | Accessible buat retail |
| Max bin/posisi | N/A (konsep tick) | 1.400 bin |
| Liquidity mining | Lewat kontrak eksternal | Built-in (2 reward token) |
| Program inti | Open source (GPL) | Closed source |

## Artinya Buat Lo

DLMM ngambil ide concentrated liquidity dan ngoptimasi end-to-end buat Solana. Hasilnya protokol di mana:

1. Posisi kecil viable (nggak ada gas yang ngerusak return lo)
2. Manajemen aktif memungkinkan (nyetel tiap hari tanpa biaya)
3. Fee mengompensasi lo buat risiko nyata (bukan rate flat)
4. LPing dan trading menyatu (posisi lo ADALAH strategi lo)

---

*Selanjutnya: Sekarang kita udah ngerti alatnya, gimana cara makenya? Strategi LP apa yang jalan di Meteora?*
