# Chapter 5: Matematika di Dalam Mesin

---

## Rumus Paling Sederhana

AMM butuh satu aturan buat nentuin harga. Inget insting Budi: *kalau orang beli, harga naik. Kalau orang jual, harga turun.*

Rumus AMM paling terkenal — yang nge-launch industri triliunan dolar — nangkep ini pake matematika SMP:

> **x × y = k**

Udah. Itu rumusnya.

Yuk kita bongkar.

## Arti x, y, dan k

Bayangin sebuah pool yang isinya dua aset: **SOL** (cryptocurrency) dan **USDC** (dolar digital, selalu ~Rp 16.000-an).

| Variabel | Artinya | Contoh |
|----------|---------|--------|
| **x** | Jumlah SOL di pool | 10 SOL |
| **y** | Jumlah USDC di pool | 2.000 USDC |
| **k** | x × y — angka ini GAK PERNAH berubah | 10 × 2.000 = **20.000** |

Pool mulai dengan 10 SOL dan 2.000 USDC. k = 20.000.

**Tugas pool:** jagain supaya x × y = 20.000, apapun trade yang terjadi.

## Sebuah Trade: Beli SOL dari Pool

Lo datang dan bilang: *"Gue mau beli 1 SOL dari pool ini. Berapa USDC yang harus gue bayar?"*

Sebelum trade lo:
- x = 10 SOL, y = 2.000 USDC
- Harga 1 SOL = y / x = 2.000 / 10 = **$200 per SOL**

Sekarang lo ambil 1 SOL keluar. Pool bakal punya 9 SOL tersisa. Tapi k harus tetep 20.000.

```
Setelah: x = 9 SOL
         x × y = 20.000
         9 × y = 20.000
         y = 20.000 / 9
         y = 2.222,22 USDC
```

Jadi y berubah dari 2.000 ke 2.222,22. Artinya **lo harus setor 222,22 USDC** buat ngambil 1 SOL.

Lo bayar 222,22 USDC buat 1 SOL. Harga "aslinya" tadi 200 USDC. Lo bayar lebih mahal.

**Harga naik karena lo beli.** Insting Budi, sekarang diformalin dalam matematika.

## Trade ke Arah Sebaliknya: Jual SOL

Sekarang orang lain datang dan jual 1 SOL ke pool.

```
Sebelum: x = 9 SOL, y = 2.222,22 USDC, harga = 2.222,22 / 9 ≈ $246,91
Setelah: x = 10 SOL
         10 × y = 20.000
         y = 2.000 USDC
```

Pool ngasih mereka 222,22 USDC buat 1 SOL mereka. Harga turun. Persis kayak kata Budi.

## Hal Penting yang Baru Lo Lihat

Coba bandingin harganya:

| Aksi | Harga Sebelum | Harga Setelah | Arah |
|------|-------------|-------------|------|
| Orang BELI SOL | $200 | $246,91 | 📈 Naik |
| Orang JUAL SOL | $246,91 | $200 | 📉 Turun |

**Rumusnya otomatis nyesuain harga berdasarkan supply dan demand.** Gak ada manusia. Gak ada order book. Gak ada lelang. Cuma x × y = k.

## Kenapa Ini Indah

Rumus ini punya sifat-sifat yang bikin dia sempurna buat pasar otomatis:

1. **Selalu bekerja.** Separah apapun orang mau trade, rumusnya selalu ngasih harga.
2. **Gak pernah habis.** Lo bisa terus trading selamanya — harganya cuma makin ekstrim aja.
3. **Bisa diprediksi.** Lo bisa ngitung persis apa yang lo dapet sebelum trade.
4. **Ada "slippage".** Trade gede ngegeser harga lebih banyak dari trade kecil. Ini mirip pasar beneran.

Poin terakhir penting. Nih contohnya:

| Ukuran Trade | SOL Dibeli | USDC Dibayar | Harga Efektif per SOL |
|-------------|-----------|-------------|---------------------|
| Kecil | 0,1 SOL | ~19,61 USDC | ~$196 |
| Sedang | 1 SOL | ~222,22 USDC | ~$222 |
| Gede | 5 SOL | ~2.000 USDC | ~$400 |

Trade makin gede, harga makin buruk. Ini namanya **price impact** atau **slippage.** Cara AMM ngelindungin diri biar gak dikuras.

## Pool sebagai Jungkat-Jungkit

Nih cara intuitif buat mikirin x × y = k:

Bayangin jungkat-jungkit dengan SOL di satu sisi dan USDC di sisi lain. Jungkat-jungkitnya harus selalu seimbang di "berat" konstan (k).

- Kalau SOL keluar dari pool (orang beli), sisi SOL jadi lebih ringan. Buat seimbang lagi, USDC harus nambah. Artinya harga SOL (USDC/SOL) NAIK.
- Kalau SOL masuk ke pool (orang jual), sisi SOL jadi lebih berat. Buat seimbang lagi, USDC harus berkurang. Harga SOL TURUN.

Cuma permainan keseimbangan doang.

## Satu Konsep yang Harus Diingat

> **x × y = k**: rumus constant product. Dia otomatis nentuin harga supaya pembelian naikin harga dan penjualan nurunin harga — persis kayak market maker manusia, tapi dijalankan murni oleh matematika.

Lo sekarang ngerti mesin yang ngejalanin hampir semua DeFi. Pool adalah pasarnya. Rumus adalah harganya. Gak perlu perantara.

---

*Selanjutnya: Pool butuh inventaris. Dari mana datangnya? Dan kenapa ada yang mau nyediain?*
