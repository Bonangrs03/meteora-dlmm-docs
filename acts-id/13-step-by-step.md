# Chapter 13: Walkthrough Step-by-Step

---

> **Reality check:** Chapter ini ngejelasin interface Meteora dApp secara konseptual. UI berubah. Tombol pindah. Prinsipnya nggak. Kalo tombol tertentu nggak ada di tempat yang gue sebutin, cari konsepnya — "bikin posisi," "pilih pool," "atur rentang" — bukan lokasi piksel tepatnya.

---

## Step 0: Sebelum Lo Nyentuh Apa-Apa

Lo butuh tiga hal:

| Apa | Kenapa | Gimana |
|-----|--------|--------|
| **Wallet Solana** | Buat nyimpen token lo dan tanda tangan transaksi | Phantom, Solflare, atau Backpack wallet |
| **Sedikit SOL** | Buat bayar transaksi (~0.000005 SOL per transaksi) | Beli di exchange, transfer ke wallet lo |
| **Token buat LP** | Aset yang bakal lo deposit ke pool | SOL + USDC adalah pair paling umum |

Buat walkthrough ini, kita asumsiin lo LP ke pool SOL-USDC. Ini pair paling liquid di Solana dan starting point paling aman.

## Step 1: Bikin/Dapet Wallet Solana

Kalo lo belum punya:

1. Buka [phantom.app](https://phantom.app) dan install browser extension (atau mobile app)
2. Bikin wallet baru
3. **Tulis seed phrase lo di kertas.** Bukan screenshot. Bukan notes app. Kertas. Simpen di tempat aman.
4. Set password kuat

## Step 2: Isi Wallet Lo

1. Beli SOL dari exchange (exchange besar manapun jual SOL)
2. Withdraw SOL ke alamat wallet lo (string panjang mulai huruf/angka — cari di Phantom di bagian "Receive" atau "Deposit")
3. Opsional, swap sebagian SOL ke USDC pake Jupiter (jup.ag) di dalam wallet lo

**Jumlah minimum buat mulai:** Dengan $20-50 senilai SOL + USDC, lo bisa buka posisi LP kecil dan pelajari mekanismenya. Di Ethereum ini impossible karena gas fee. Di Solana, ini nyata.

## Step 3: Navigasi ke Meteora

1. Buka [app.meteora.ag](https://app.meteora.ag)
2. Connect wallet lo (klik "Connect Wallet" di kanan atas, pilih Phantom)
3. Setujui koneksi di popup wallet lo

## Step 4: Cari Pool Lo

Lo bakal liat interface Meteora dengan berbagai pool terdaftar. Buat posisi pertama lo:

1. Klik tab **"Pools"** atau **"DLMM"**
2. Cari **SOL-USDC**
3. Lo bakal liat beberapa pool SOL-USDC dengan bin step beda (misal 5 bps, 20 bps, 50 bps)

**Bin step mana yang dipilih buat posisi pertama lo:**

| Bin Step | Artinya | Rekomendasi |
|----------|---------|-------------|
| 5 bps | Sangat ketat, sangat efisien | Skip dulu — terlalu agresif |
| 20 bps | Menengah, pilihan populer | Starting point bagus |
| 50 bps+ | Lebih lebar, lebih forgiving | Aman buat pemula |

Pilih pool SOL-USDC dengan 20 atau 50 bps.

## Step 5: Periksa Poolnya

Sebelum deposit, liat:

- **Harga saat ini:** Lagi di harga berapa SOL sekarang?
- **Volume 24j:** Seberapa banyak aktivitas trading? Lebih banyak volume = lebih banyak fee.
- **TVL (Total Value Locked):** Seberapa banyak likuiditas udah ada di pool ini? TVL lebih tinggi artinya porsi fee pie lebih kecil buat lo, tapi juga lebih stabil.
- **Fee 24j:** Berapa yang LP dapet kemarin?
- **APR:** Estimasi return tahunan (ini fluktuatif — jangan terlalu fixated)

## Step 6: Buka Posisi

1. Klik **"Create Position"** atau tombol **"+"**
2. Lo bakal liat chart dengan harga saat ini dan tangga bin

### Step 6a: Pilih Strategi Lo

Interface Meteora ngasih preset:

| Preset | Fungsinya |
|--------|-----------|
| **Spot** | Distribusi merata di rentang yang lo pilih |
| **Curve** | Terkonsentrasi di sekitar harga saat ini |
| **Bid-Ask** | Lebih berat di satu sisi |

Buat posisi PERTAMA lo, pilih **Spot** dengan rentang menengah.

### Step 6b: Atur Rentang Lo

- Liat harga saat ini (anggep SOL lagi $200)
- Atur harga minimum lo (misal $180 — 10% di bawah harga saat ini)
- Atur harga maksimum lo (misal $220 — 10% di atas harga saat ini)
- Interface nunjukin berapa bin yang tercakup

**Panduan lebar rentang:**

| Lebar Rentang | Level Risiko | Maintenance |
|---------------|-------------|-------------|
| ±2-5% | Tinggi | Cek harian |
| ±5-15% | Menengah | Cek setiap beberapa hari |
| ±20%+ | Rendah | Cek mingguan |

### Step 6c: Masukin Jumlah Deposit Lo

- Lo bisa deposit dua token sama banyak (butuh punya keduanya)
- Atau deposit satu token dan biarin interface yang handle swap (mungkin kena biaya kecil)
- Mulai kecil — total nilai $20-50 buat posisi pertama lo

## Step 7: Review dan Konfirmasi

Sebelum pencet konfirmasi, cek:

1. **Rentang harga:** Udah sesuai yang lo mau?
2. **Jumlah:** Lo nyaman kehilangan ini kalo terjadi hal buruk?
3. **Bin step dan fee:** Struktur fee-nya masuk akal?
4. **Estimasi APR:** Apakah reasonable (bukan angka gila)?

Kalo udah siap, klik **"Create Position"** atau **"Deposit."**

Wallet lo bakal minta lo setujui transaksi. Fee-nya sekitar ~0.000005 SOL (pecahan sen). Konfirmasi.

## Step 8: Lo Sekarang LP

Posisi lo live. Lo bakal liat di dashboard Meteora lo dengan:

- Nilai posisi lo saat ini (dalam USD)
- Rentang (harga min-max)
- Fee yang belum diklaim (ini ngumpul real-time)
- Status: "In Range" (dapet fee) atau "Out of Range" (nggak dapet)

## Step 9: Apa yang Dilakuin Selanjutnya

### Langsung:
- Bookmark URL posisi lo atau screenshot alamat pool
- Catat harga SOL saat ini — ini titik referensi lo buat ngukur IL nanti

### 24 jam pertama:
- Cek berapa fee yang udah lo dapet (bahkan di posisi $50, lo bakal liat pecahan sen ngumpul — itu duit beneran dari trade beneran)
- Observasi apakah posisi lo tetap in range

### Minggu pertama:
- Kalo harga mendekati batas rentang lo, pertimbangin buat nyetel (melebarin atau mindahin rentang lo)
- Klaim fee lo kalo pengen liat yield compound (atau biarin aja — mereka bakal tetap di pool)

---

## Step 10: Ngatur Posisi Lo

### Cara Klaim Fee

1. Buka posisi lo
2. Klik "Claim Fees" atau cari bagian fees
3. Setujui transaksi di wallet lo
4. Fee dikirim ke wallet lo

### Cara Nyetel Rentang Lo

1. Buka posisi lo
2. Klik "Edit" atau "Adjust Position"
3. Geser slider rentang ke rentang baru yang lo mau
4. Konfirmasi transaksi

### Cara Nutup Posisi Lo

1. Buka posisi lo
2. Klik "Close Position" atau "Withdraw"
3. Lo bakal nerima bagian lo dari aset pool saat ini
4. PENTING: Aset yang lo terima nggak bakal dalam rasio yang sama kayak pas lo deposit. Ini impermanent loss jadi permanent. Bandingin nilainya sama apa yang lo bakal punya kalo cuma hold.

---

## Kebiasaan Paling Penting

Setiap kali lo nutup posisi, lakuin perhitungan ini:

```
Yang gue terima pas nutup:    X SOL + Y USDC = $Z
Yang gue bakal punya kalo cuma hold: SOL awal × harga SOL saat ini + USDC awal = $W

Kalo Z > W: lo untung (fee melebihi IL)
Kalo Z < W: lo rugi (IL melebihi fee)
Kalo Z = W: lo balik modal di posisi, dapet ilmu
```

Kebiasaan satu ini — membandingkan hasil aktual lo ke baseline "cuma hold" — yang misahin LP profitable dari yang kehilangan duit tanpa ngerti kenapa.

---

*Selanjutnya: Gimana cara lo track performa dari waktu ke waktu? Tools apa yang ngebantu? Kapan lo tau waktunya exit?*
