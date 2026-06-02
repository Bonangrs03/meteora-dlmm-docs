# Chapter 10: Masuk ke Meteora DLMM

---

## Evolusi Berikutnya

Kita udah bangun, selangkah demi selangkah:

- Chapter 5: Rumus AMM x × y = k — pool yang trading otomatis
- Chapter 9: Concentrated liquidity — naruh duit lo cuma di tempat yang penting

Sekarang: gimana kalo kita ambil concentrated liquidity dan bangun ulang dari nol — khusus buat blockchain dengan fee hampir nol dan finalitas sub-detik?

Itulah Meteora DLMM.

## Kepanjangan DLMM

**D**ynamic **L**iquidity **M**arket **M**aker.

Setiap kata punya arti:

| Kata | Artinya |
|------|---------|
| **Dynamic** | Fee menyesuaikan kondisi market. Makin volatile = fee makin tinggi. |
| **Liquidity** | Ini soal nyediain aset buat trading — sama kayak Budi. |
| **Market Maker** | Gantiin perantara manusia dengan kode — sama kayak AMM. |

## Ide Inti: Bin

Inget gimana concentrated liquidity (Chapter 9) ngasih lo pilihan harga? DLMM ngambil ini lebih jauh dengan membagi rentang harga jadi langkah-langkah diskrit yang disebut **bin.**

Bayangin tangga. Setiap anak tangga adalah harga spesifik. Likuiditas lo duduk di anak tangga tertentu.

```
Tangga Harga buat pool SOL-USDC:

$180.00  ← Bin 0
$180.50  ← Bin 1    (kalo bin step = 0.25%)
$181.00  ← Bin 2
$181.50  ← Bin 3
$182.00  ← Bin 4     ← HARGA SAAT INI (Active Bin)
$182.50  ← Bin 5
$183.00  ← Bin 6
  ...
```

Cuma SATU bin yang aktif dalam satu waktu — bin tempat harga market saat ini berada. Di situlah semua trading terjadi.

## Yang Terjadi di Dalam Satu Bin

Ini yang mengejutkan: trade di dalam satu bin punya **zero price impact.**

Inget Chapter 5, setiap trade menggerakkan harga di AMM tradisional? Di sini nggak. Di dalam satu bin, harga tetap. Lo bisa trading sampai kapasitas bin itu habis di harga yang persis sama.

Harga cuma berubah ketika satu bin terkuras habis dan active bin pindah ke bin berikutnya — kayak melangkah ke anak tangga berikutnya.

Ini artinya DLMM ngasih harga lebih baik buat trader (nggak ada slippage buat trade kecil) sambil tetap melindungi LP (harga nggak bisa kabur dalam satu bin).

## Bin Step

Jarak antar bin disebut **bin step,** diukur dalam basis points (bps).

> 1 bp = 0.01%

| Bin Step | Jarak Harga (di SOL $200) | Paling Cocok Buat |
|----------|--------------------------|-------------------|
| 1 bps (0.01%) | $0.02 | Pair stabil (USDC-USDT) — sangat ketat, sangat presisi |
| 10 bps (0.10%) | $0.20 | Pair utama (SOL-USDC) — seimbang |
| 25 bps (0.25%) | $0.50 | Volatilitas menengah |
| 100 bps (1%) | $2.00 | Pair volatil — cakupan lebih luas |
| 400 bps (4%) | $8.00 | Volatilitas ekstrem — rentang maksimum |

**Bin step lebih kecil = tangga lebih rapat, lebih presisi, capital efficiency lebih tinggi** (kalo lo nebak rentang yang tepat).
**Bin step lebih besar = cakupan per bin lebih luas,** lebih cocok buat aset volatil yang harganya gerak cepet.

Ini pilihan yang lo buat pas nyediain likuiditas — dan ini salah satu keputusan paling penting.

## Dynamic Fee: Harga yang Ngerti Market

Kebanyakan AMM narik fee tetap di setiap trade (0.3%, 1%, dll). Market lagi tenang atau kacau — fee sama aja.

Fee DLMM itu **dinamis.** Ada dua komponen:

### 1. Base Fee (Selalu Dikenakan)

Fee minimum, ditetapkan pas pool dibuat. Tergantung bin step dan beberapa parameter pool. Anggap aja ini "harga dasar."

### 2. Variable Fee (Bonus Volatilitas)

Pas market lagi volatil — pas trade nyebrang banyak bin, pas harga gerak cepet — variable fee ikut naik. Pas market tenang lagi, dia turun balik ke nol.

**Total Fee = Base Fee + Variable Fee** (maksimal 10%)

### Kenapa Ini Penting

| Kondisi Market | Yang Terjadi ke Fee | Alasannya |
|----------------|---------------------|-----------|
| Tenang, sideways | Fee rendah (deket base) | Narik lebih banyak volume trading |
| Volatil, gerak cepet | Fee tinggi (base + variable) | Lindungin LP dari arbitrage |
| Volatilitas ekstrem | Fee sangat tinggi | Kompensasi LP atas risiko impermanent loss |

Ini cerdas. Di keuangan tradisional, market maker melebarkan spread pas periode volatil. DLMM ngelakuin hal yang sama secara otomatis.

Bayangin gini: pas market lagi tenang, toko lo buka dengan harga kompetitif. Pas badai datang dan semua orang panik, lo naikin harga karena melayani pelanggan jadi lebih berisiko. Masuk akal, kan?

## Pengumpulan Fee: Lo Pilih Dibayar Pakai Apa

Pas lo dapet fee sebagai LP, DLMM ngasih dua pilihan:

| Mode | Yang Lo Terima |
|------|---------------|
| **Input Only** | Fee dibagi antara dua token — lo dapet sebagian SOL dan sebagian USDC. Seimbang. |
| **Only Y** | Semua fee dibayar dalam quote token (USDC di pool SOL-USDC). Lo cuma ngumpulin USDC. |

Kenapa lo milih "Only Y"? Kalo lo yakin SOL bakal naik, lo mungkin pengen fee lo dalam USDC biar nggak dipaksa megang lebih banyak SOL di harga yang mungkin udah kemahalan. Atau mungkin lo cuma pengen pendapatan stablecoin yang predictable tanpa nambah exposure SOL lo.

Detail kecil yang ngasih lo lebih banyak kontrol.

## Bin Dikelompokkan: Bin Array

Di belakang layar, bin diatur dalam kelompok berisi 70 yang disebut **BinArray.** Ini optimasi teknis — lo nggak perlu khawatir sebagai user, tapi ini ngejelasin kenapa lo liat batasan tertentu di UI.

Pool default bisa nge-handle trade sekitar 1.024 bin array (dari indeks -512 sampai +511), mencakup rentang harga yang sangat besar. Buat kasus ekstrem, mekanisme ekstensi nge-handle bin yang jauh di luar rentang itu.

## Satu Konsep yang Perlu Diingat

> **DLMM** = concentrated liquidity yang diatur jadi bin harga diskrit (kayak tangga), dengan dynamic fee yang naik pas volatilitas dan turun pas market tenang.

Lo naruh likuiditas lo ke bin spesifik di sekitar harga saat ini. Cuma active bin yang memproses trade. Pas bin itu terkuras, tangga pindah ke bin berikutnya. Fee lo menyesuaikan seberapa gilanya market.

---

*Selanjutnya: Gimana DLMM beda dari Uniswap V3 (protokol concentrated liquidity paling terkenal)? Apa yang bikin dia cocok banget buat Solana?*
