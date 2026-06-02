# Bab 3: Spread Sebagai Bisnis

---

## Penjual Pulsa di Terminal Bus

Ada seorang bapak namanya Budi yang jualan pulsa di terminal bus yang ramai di Jakarta.

Dia beli pulsa secara grosir dari provider:
- **Harga modal dia:** Rp 9.800 per voucher Rp 10.000

Dia jual ke penumpang:
- **Harga jual dia:** Rp 10.200 per voucher Rp 10.000

Spread-nya Rp 400. Itu seluruh model bisnisnya.

## Keseharian Budi

| Waktu | Pelanggan | Voucher Terjual | Pendapatan (Spread × Qty) |
|------|-----------|---------------|------------------------|
| Pagi (6-10) | Ramai banget | 150 | Rp 60.000 |
| Siang (10-2) | Sepi | 40 | Rp 16.000 |
| Sore (2-6) | Stabil | 90 | Rp 36.000 |
| Malam (6-10) | Ramai banget | 140 | Rp 56.000 |
| **Total** | | **420** | **Rp 168.000** |

Budi dapet sekitar Rp 168.000 per hari cuma dari spread. Lumayan lah buat jualan pulsa di terminal.

Tapi coba kita liat lebih deket apa yang bikin ini berhasil — dan apa yang bisa ngerusak.

## Tiga Hal yang Menentukan Profit Budi

### 1. Spread (Lebar)

Kalau Budi ngelebarin spread-nya — beli di Rp 9.500, jual di Rp 10.500 — dia dapet Rp 1.000 per voucher, bukan Rp 400.

Tapi ada masalah: penumpang bakal sadar. Penjual pulsa di seberang terminal jual di Rp 10.100. Pelanggan Budi pindah ke sana.

**Spread lebih lebar = lebih banyak profit per transaksi, tapi lebih sedikit transaksi.**

### 2. Volume Trading (Berapa Banyak Transaksi)

Kalau terminal bus tiba-tiba dapet penumpang dua kali lipat, Budi jual voucher dua kali lipat. Spread-nya gak berubah, tapi volumenya dobel. Penghasilan hariannya dobel.

**Lebih banyak volume = lebih banyak profit, dengan spread yang sama.**

### 3. Risiko Inventori

Budi nyimpen voucher pulsa senilai Rp 5.000.000 di tasnya. Itu inventori dia.

Suatu hari, provider ngumumin promosi: pulsa sekarang Rp 8.000 per voucher buat semua orang. Inventori Budi yang Rp 5.000.000 tiba-tiba nilainya turun. Dia bayar Rp 9.800 buat voucher yang sekarang cuma bernilai Rp 8.000 di pasar terbuka. Itu namanya **rugi.**

> **Risiko inventori** = bahaya bahwa nilai barang yang lo pegang turun ketika lo lagi megang.

## Ketegangan Mendasar Jadi Market Maker

Budi menghadapi tradeoff tiga arah yang konstan:

```
         SPREAD LEBIH LEBAR
               ↑
              / \
             /   \
            /     \
VOLUME LEBIH       RISIKO INVENTORI
SEDIKIT            LEBIH BESAR
(harga lebih       (spread lebih lebar =
tinggi menakuti    perputaran lebih lambat
pembeli)           = megang lebih lama)
```

Setiap market maker sepanjang sejarah — dari Budi di terminal bus sampe perusahaan trading terbesar di Wall Street — menghadapi segitiga yang persis sama ini.

## Apa yang Bikin Pasar Jadi "Bagus"

Pasar yang bagus buat market maker punya:

| Faktor | Kenapa membantu | Terminal Budi? |
|--------|-------------|------------------|
| **Volume alami tinggi** | Banyak transaksi tanpa perlu ngelebarin spread | ✓ (terminal ramai) |
| **Harga aset stabil** | Risiko inventori lebih kecil | ✓ (harga pulsa stabil) |
| **Kompetisi wajar** | Jaga spread tetap adil tapi gak setipis silet | ✓ (satu kompetitor, bukan dua puluh) |
| **Overhead rendah** | Lebih banyak profit yang disimpen per transaksi | ✓ (cuma modal tas dan kursi) |

## Apa yang Bikin Pasar Jadi "Jelek"

| Faktor | Kenapa merugikan | Contoh dunia nyata |
|--------|-------------|-------------------|
| **Volume rendah** | Harus ngelebarin spread buat survive, yang makin matiin volume | Jualan koleksi langka |
| **Aset volatil** | Nilai inventori naik-turun liar | Trading memecoin baru |
| **Terlalu banyak kompetisi** | Spread keperes sampe hampir nol | Pair mata uang mayor (EUR/USD) |
| **Overhead tinggi** | Harus dapet cukup buat nutup biaya sebelum profit | Jalanin toko fisik |

## Dari Budi ke Miliaran

Ini yang gila: perusahaan keuangan terbesar di dunia beroperasi dengan prinsip yang persis sama kayak Budi.

Citadel Securities, salah satu firma market-making terbesar secara global, nanganin sekitar 27% dari seluruh volume trading saham AS. Model bisnis mereka? Beli di bid, jual di ask, kantongin spread — jutaan kali per hari.

Permainan yang sama. Skala yang beda.

| | Budi | Citadel Securities |
|---|---|---|
| Aset | Voucher pulsa | Saham |
| Volume harian | 420 transaksi | ~7 miliar lembar saham |
| Spread per transaksi | Rp 400 | Pecahan sen |
| Dapet duit karena... | Spread × Volume | Spread × Volume |
| Risiko | Perubahan harga provider | Harga saham anjlok |

Matematikanya identik: **Profit = Spread × Volume − Kerugian Inventori**

## Satu Konsep yang Harus Diinget

**Bisnis market maker = lebar spread × volume trading, diseimbangkan dengan risiko inventori.** Setiap keputusan — seberapa lebar spread dipasang, aset apa yang ditrading, berapa banyak inventori dipegang — semua soal ngatur tradeoff ini.

---

*Selanjutnya: Gimana kalau kita ganti Budi dengan program komputer? Kayak apa tuh programnya?*
