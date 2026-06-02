# Chapter 8: Kenapa Solana Ngubah Permainan

---

## Biaya Sebuah Trade

Ngobrolin sesuatu yang kedengerannya membosankan tapi ngubah segalanya: **biaya transaksi.**

Setiap kali orang trading di pool AMM, trade itu terjadi sebagai transaksi di blockchain. Dan blockchain ngecharge fee buat proses transaksi.

Berapa besar fee itu nentuin **siapa yang mampu jadi LP.**

## Dua Dunia

| | Ethereum | Solana |
|---|---|---|
| **Fee per trade** | $5–50 (kadang $100+) | ~$0,0002 (sepersekian sen) |
| **Waktu konfirmasi** | ~12 detik | ~0,4 detik |
| **Trade per detik** | ~15–30 | ~3.000+ (teoritis) |
| **Yang $1 bisa beli** | Paling 0,2 trade | ~5.000 trade |

Ini bukan perbedaan kecil. Ini perbedaan *struktural* yang sepenuhnya ngubah siapa yang bisa ikut.

## Kenapa Ini Penting Buat LP

Bayangin lo LP dengan $100 buat dideploy.

**Di Ethereum:**
- Lo setor $100 lo ke pool.
- Selama sebulan, bagian lo dapet $8 dalam fee. (return 8% — lumayan!)
- Tapi pas lo mau tarik, rebalance, atau compound, transaksi itu cost $12 dalam gas.
- Return bersih lo: $8 − $12 = **−$4.** Lo rugi.

**Di Solana:**
- Lo setor $100 lo.
- Lo dapet $8 dalam fee.
- Lo compound penghasilan lo 10 kali, masing-masing cost $0,0002.
- Return bersih lo: $8 − $0,002 = **+$7,998.**

Di Ethereum, LP kecil hancur karena fee. Di Solana, mereka bisa ikut dengan untung.

## Matematika LP di Masing-masing Chain

Anggap lo mau aktif ngelola posisi LP — rebalancing, compounding, nyesuain price range:

| Aksi | Biaya Ethereum | Biaya Solana |
|------|--------------|-------------|
| Buka posisi | $8 | $0,0002 |
| Rebalance (sesuain range) | $8 | $0,0002 |
| Klaim fee | $6 | $0,0002 |
| Compound (reinvest fee) | $10 | $0,0002 |
| Tutup posisi | $8 | $0,0002 |
| **Total per siklus** | **$40** | **$0,001** |

Kalau lo ngelakuin ini mingguan, Ethereum cost lo $2.080/tahun dalam gas. Solana cost lo $0,05/tahun.

## Concentrated Liquidity Butuh Manajemen Aktif

Nih koneksi kuncinya (kita bakal jelasin concentrated liquidity secara penuh di Chapter 9):

Beberapa strategi LP maksa lo buat sering nyesuain posisi — mindahin price range pas pasar gerak, klaim dan reinvest fee, rebalance pas harga geser.

Di Ethereum, cuma whales yang mampu ngelakuin ini. Fee rebalance $10 di posisi $10.000 itu 0,1% — nyebelin tapi bisa ditahan. Di posisi $200, itu 5% — bencana.

Di Solana, fee-nya efektif nol. **Siapa aja bisa aktif ngelola posisi LP mereka.** Ini nge-demokratisasi seluruh kategori strategi yang sebelumnya cuma bisa diakses institusi dan whales.

## Di Luar Fee: Arsitektur Solana

Fee rendah Solana bukan kebetulan. Ini datang dari pilihan desain fundamental:

| Pilihan Desain | Artinya |
|---------------|--------|
| **Proof of History (PoH)** | Jam built-in yang ngasih timestamp transaksi tanpa nunggu konsensus soal timing. Ngehilangin bottleneck besar. |
| **Eksekusi paralel** | Solana bisa proses ribuan transaksi secara bersamaan, bukan satu per satu. Kayak jalan tol 20 lajur vs jalan satu lajur. |
| **Gak ada kongesti mempool** | Di Ethereum, lo bidding lawan orang lain buat masukin transaksi lo. Di Solana, transaksi diproses begitu dateng. |

Hasilnya: Solana memproses lebih banyak transaksi dalam sehari dibanding Ethereum dalam setahun — dengan biaya yang jauh lebih kecil.

## Ekosistemnya: Siapa yang di Solana?

Per pertengahan 2026, ekosistem DeFi Solana nyimpen sekitar $5,25 miliar dalam total value locked (TVL) dan memproses sekitar $1 miliar volume DEX per hari.

| Protokol | Peran | Volume Harian (perkiraan) |
|----------|------|-------------------------|
| **Jupiter** | Agregator DEX (nyari harga terbaik di semua pool) | Ngerutekan mayoritas volume Solana |
| **Raydium** | AMM tradisional (constant product, kayak Uniswap V2) | ~$150M |
| **Orca** | AMM concentrated liquidity (kayak Uniswap V3) | ~$176M |
| **Meteora** | DLMM (concentrated liquidity berbasis bin) | ~$152M |

Meteora, protokol yang kita pelajari, adalah DEX terbesar ke-4 di Solana berdasarkan volume — dan dia berkembang lebih cepat dari kebanyakan karena desain uniknya.

## Kenapa Solana + Concentrated Liquidity = Pasangan Sempurna

Strategi concentrated liquidity butuh:
- Penyesuaian posisi yang sering (mindahin range)
- Klaim fee dan reinvest yang sering
- Kadang rebalancing harian atau bahkan per jam

Semua ini mustahil di chain mahal buat orang biasa. Di Solana, ini remeh.

> **Solana bikin strategi LP aktif bisa diakses siapa aja dengan HP dan $20.**

Ini kenapa protokol LP paling inovatif — termasuk Meteora DLMM — dibangun di Solana, bukan Ethereum. Arsitektur chain-nya cocok sama kebutuhan strateginya.

## Satu Konsep yang Harus Diingat

**Biaya transaksi adalah barrier to entry.** Di chain dengan fee tinggi, cuma modal gede yang bisa LP dengan untung. Di Solana, fee hampir nol artinya siapa aja bisa ikut — dan itu ngubah strategi LP mana yang layak.

---

*Selanjutnya: Ide besar yang bikin LPing jauh lebih capital-efficient. Concentrated liquidity.*
