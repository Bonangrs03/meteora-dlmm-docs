# Chapter 12: Strategi LP di Meteora

---

## Sekarang Lo Udah Ngerti Alatnya

Lo ngerti:
- Apa itu likuiditas (Ch 1)
- Apa yang dilakukan market maker (Ch 2-3)
- Gimana AMM bekerja (Ch 4-5)
- Dari mana duit LP berasal (Ch 6)
- Biaya tersembunyi impermanent loss (Ch 7)
- Kenapa Solana penting (Ch 8)
- Concentrated liquidity (Ch 9)
- Gimana bin DLMM dan dynamic fee bekerja (Ch 10)
- Gimana DLMM beda dari alternatif (Ch 11)

Sekarang: **gimana cara lo beneran bikin duit dengannya?**

## Spektrum Strategi

Strategi DLMM jatuh di spektrum dari "pasang dan lupakan" sampai "aktif ngatur tiap jam."

```
USAHA RENDAH ←————————————————————————→ USAHA TINGGI
   Wide/Chill    Spot    Curve    Bid-Ask    20-Bin   Dynamic Vaults
```

Masing-masing punya profil risk-reward yang beda. Mari kita bahas satu-satu.

---

## Strategi 1: Wide Range / "Chill"

**Apa itu:** Sebar likuiditas lo di rentang harga yang sangat lebar (misal ±20-30% dari harga saat ini).

**Cara kerjanya:**
- Lo pilih rentang lebar di sekitar harga saat ini
- Likuiditas lo aktif selama harga tetap di rentang itu
- Lo hampir nggak perlu ngecek

**Paling cocok buat:** Pair stabil (USDC-USDT), pair yang lo yakin bakal trading dalam rentang untuk waktu lama, atau kalo lo cuma pengen deposit dan lupakan.

**Kelebihan:**
- Maintenance sangat rendah
- Jarang keluar dari rentang
- Starting point bagus buat pemula

**Kekurangan:**
- Capital efficiency lebih rendah (duit lo tersebar tipis)
- Fee yang didapat lebih rendah dari strategi terkonsentrasi
- Tetep kena impermanent loss kalo harga gerak jauh

**Analogi:** Lo adalah toko yang jual segalanya dari Rp 1.000 sampai Rp 1.000.000. Kebanyakan pelanggan nggak bakal beli di ujung ekstrem, tapi toko lo selalu buka.

---

## Strategi 2: Spot (Distribusi Seragam)

**Apa itu:** Sebar likuiditas merata di rentang menengah (misal ±5-10%).

**Cara kerjanya:**
- Lo pilih rentang di sekitar harga saat ini
- Likuiditas didistribusiin seragam ke semua bin di rentang lo
- Strategi default dan paling umum

**Paling cocok buat:** General purpose. Bagus pas lo nggak punya pandangan arah yang kuat. Strategi "gue rasa harganya bakal di sekitar sini."

**Variasi:**
| Nama | Jumlah Bin | Lebar Rentang | Use Case |
|------|-----------|-------------|----------|
| Spot-Concentrated | 1-3 bin | Sangat ketat | Hampir pasti harga stabil |
| Spot-Spread | 20-30 bin | Menengah | Pendekatan seimbang |
| Spot-Wide | ~50 bin | Lebar | Lebih aman, kurang efisien |

**Kelebihan:** Simpel, versatile, seimbangin efisiensi dengan keamanan.
**Kekurangan:** Nggak optimal buat kondisi market tertentu.

---

## Strategi 3: Curve (Terkonsentrasi di Tengah)

**Apa itu:** Sebagian besar likuiditas lo terkonsentrasi ketat di sekitar harga saat ini, dengan lebih sedikit di pinggiran.

**Cara kerjanya:**
- Lo naruh likuiditas tebal persis di active bin
- Likuiditas lebih sedikit di bin yang lebih jauh
- Capital efficiency maksimum pas harga tetap deket tengah

**Paling cocok buat:** Pair stabil (USDC-USDT), atau pair apapun pas periode volatilitas sangat rendah.

**Kelebihan:**
- Fee tertinggi pas harga tetap di rentang
- Capital efficiency maksimum

**Kekurangan:**
- Cepet keluar rentang kalo harga gerak
- Butuh monitoring lebih sering
- Impermanent loss paling parah kalo harga trending kuat

**Analogi:** Lo adalah coffee shop yang buka 24/7 tapi cuma nyajiin satu jenis kopi spesifik. Pas lingkungan sekitar pengen persis kopi itu, lo cuan gede. Pas selera berubah, lo sepi.

---

## Strategi 4: Bid-Ask (Directional)

**Apa itu:** Distribusi asimetris — lebih banyak likuiditas di satu sisi daripada sisi lainnya.

**Cara kerjanya:**
- Kalo lo pikir harga bakal NAIK: naruh lebih banyak likuiditas di ATAS harga saat ini (jual pas naik)
- Kalo lo pikir harga bakal TURUN: naruh lebih banyak likuiditas di BAWAH harga saat ini (beli pas turun)
- Sisi yang lebih tipis tetep dapet sebagian fee

**Paling cocok buat:** Pas lo punya pandangan arah. Lo pengen ngumpulin satu aset atau keluar dari aset lain.

**Kelebihan:**
- Bertindak sebagai DCA otomatis (dollar-cost averaging)
- Lo dapet fee sambil nunggu harga target lo
- Gabungin strategi trading dengan yield LP

**Kekurangan:**
- Butuh penilaian market
- Kalo lo salah soal arah, lo kehilangan peluang fee di sisi satunya

**Analogi:** Lo di pasar buah. Lo yakin harga mangga bakal naik minggu depan. Lo naruh lebih banyak ruang lapak lo buat beli mangga sekarang (di harga lebih rendah) sambil tetep jual sebagian dengan markup.

---

## Strategi 5: Strategi 20-Bin (Meta Saat Ini)

Ini dapet perhatian khusus karena udah populer di komunitas Meteora LP per 2026.

**Apa itu:** Konfigurasi spesifik: rentang 20-bin dengan bin step lebih kecil (seringnya 20 bps atau kurang), targetnya capture fee frekuensi tinggi.

**Cara kerjanya:**
- Lo pake sekitar 20 bin terpusat di sekitar harga saat ini
- Bin step kecil artinya granularitas harga ketat
- Idenya: tangkep banyak trade kecil dengan capital efficiency tinggi

**Kenapa populer:**
- Keseimbangan bagus antara efisiensi dan keamanan rentang
- Jalan baik buat pair volatilitas menengah
- Diuji dan didiskusiin ekstensif oleh komunitas

**Contoh nyata:** Pas periode trading aktif, beberapa posisi 20-bin di pair volatil pernah nangkep fee harian mendekati 10% dari nilai posisi. Return ini TIDAK typical atau sustainable — terjadi pas burst pendek volume ekstrem — tapi nunjukin apa yang mungkin pas lo posisi dengan benar selama volatilitas.

**Kendalanya:** Periode return tinggi ini episodik. Posisi yang dapet 10% sehari mungkin dapet 0.3% di hari berikutnya.

---

## Strategi 6: Single-Sided / DCA

**Apa itu:** Deposit cuma SATU jenis token ke bin tertentu (atau rentang sempit).

**Cara kerjanya:**
- Lo deposit cuma USDC ke bin di atas harga saat ini → bertindak sebagai limit sell order
- Lo deposit cuma SOL ke bin di bawah harga saat ini → bertindak sebagai limit buy order
- Pas harga nyampe bin lo, token lo berubah ke token satunya

**Paling cocok buat:** Ngumpulin aset di harga target tanpa mantengin chart. Atau keluar di harga target.

**Kelebihan:**
- Entry/exit otomatis, bebas emosi
- Nggak ada impermanent loss (lo cuma megang satu aset)
- Lo dapet fee sambil limit order lo nunggu

**Kekurangan:**
- Kalo harga nggak pernah nyampe bin lo, lo nggak dapet apa-apa
- Opportunity cost: modal lo terikat, nggak available buat kegunaan lain

---

## Gimana Cara Milih: Framework Keputusan

Tanyain diri lo pertanyaan ini:

### 1. Seberapa stabil pair ini?

| Tipe Pair | Contoh | Strategi Disarankan |
|-----------|--------|---------------------|
| Stable-stable | USDC-USDT | Curve, rentang sangat ketat |
| Pair utama | SOL-USDC | Spot spread (20-50 bin) |
| Volatil | Memecoin-USDC | Wide, atau Bid-Ask |
| Token baru | Launch pool | Sangat lebar, atau single-sided |

### 2. Seberapa banyak waktu lo?

| Komitmen Waktu | Strategi |
|----------------|----------|
| Cek seminggu sekali | Wide / Chill |
| Cek harian | Spot |
| Cek beberapa kali/hari | Curve, Bid-Ask |
| Monitor aktif | 20-Bin, Dynamic Vaults |

### 3. Apa pandangan market lo?

| Pandangan | Strategi |
|-----------|----------|
| "Bakal stay di rentang" | Spot, Curve |
| "Bakal naik" | Bid-Ask (lebih banyak di atas harga saat ini) |
| "Bakal turun" | Bid-Ask (lebih banyak di bawah harga saat ini) |
| "Gue pengen beli di harga X" | Single-sided di bawah X |
| "Gue pengen jual di harga Y" | Single-sided di atas Y |
| "Nggak tau" | Wide / Chill |

---

## Manajemen Risiko: Yang Nggak Bisa Ditawar

Sebelum lo deploy satu dolar pun:

### 1. Cek Total Fee yang Dihasilkan

Metrik paling penting, menurut LP Meteora berpengalaman: **total fee yang udah dihasilkan pool secara historis.**

Pool yang udah ngumpulin 500 SOL dalam cumulative fee jauh lebih terpercaya daripada yang cuma 5 SOL. Total fee rendah sering nunjukin volume asli rendah — atau lebih parah, volume palsu yang dirancang buat narik LP.

> **Rule of thumb:** Jangan LP ke pool dengan total fee kurang dari 25 SOL.

### 2. Periksa Tokennya

Kalo lo LP ke token yang lo nggak terlalu kenal:

- Cek Rugcheck.xyz buat keamanan kontrak token
- Cek Bubblemaps buat konsentrasi supply (kalo 3 wallet megang 90% supply, kabur)
- Liat chart — apa ada riwayat trading nyata atau cuma pump?
- Cek channel sosial — apa ada komunitas nyata atau cuma bot?

### 3. Mulai Kecil

Posisi pertama lo harus jumlah yang lo rela kehilangan sepenuhnya. Anggap sebagai biaya belajar. Pelajari mekanismenya, observasi gimana fee ngumpul, alamin impermanent loss secara real-time — dengan duit yang nggak bakal nyakitin.

### 4. Jangan Kejar APR Ekstrem

Kalo pool nunjukin 1000% APR, tanya: kenapa? Biasanya karena:
- Tokennya volatil dan lo bakal hancur kena IL
- Volumenya temporer (hype peluncuran token)
- Ada risiko tersembunyi yang nggak lo liat

Return sustainable datang dari volume trading asli yang konsisten — bukan spike hype.

---

## Satu Konsep yang Perlu Diingat

Pilihan strategi lo ngejawab tiga pertanyaan sekaligus:
- Seberapa banyak yang bakal lo dapet (konsentrasi fee)
- Seberapa banyak yang bakal lo ilangin kalo harga gerak (exposure IL)
- Seberapa banyak perhatian yang perlu lo kasih (frekuensi manajemen)

Nggak ada strategi terbaik — cuma strategi yang cocok sama modal lo, waktu lo, dan toleransi risiko lo.

---

*Selanjutnya: Buka aplikasinya. Ayo beneran lakuin ini. Step by step.*
