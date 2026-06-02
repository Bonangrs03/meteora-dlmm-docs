# Chapter 14: Monitoring, Exit, dan Ngukur Profit

---

## Siklus Hidup LP

LPing itu bukan "deposit dan lupakan." Ini siklus:

```
DEPOSIT → MONITOR → PUTUSIN → (SETEL atau EXIT) → EVALUASI → DEPOSIT LAGI
```

Chapter ini ngebahas tiga langkah tengah: monitor, putusin, bertindak.

## Monitoring: Apa yang Harus Dipantau

### Cek Harian (30 detik)

Buka posisi lo. Tanya tiga pertanyaan:

1. **Posisi gue in range?** Kalo iya → dapet fee. Kalo nggak → nggak dapet. Simpel.
2. **Seberapa deket harga ke batas rentang gue?** Kalo mendekat, lo perlu putusin segera.
3. **Berapa fee yang gue dapet hari ini?** Bandingin ke nilai posisi. 0.1% harian = 36% annualized (kalo sustained).

### Review Mingguan (5 menit)

| Metrik | Yang Dicek | Kenapa |
|--------|-----------|--------|
| **PnL Posisi** | Nilai saat ini vs nilai "cuma hold" | Profit/rugi lo yang sebenernya |
| **Fee APR** | Fee minggu ini ÷ nilai posisi × 52 | Apakah yield-nya sustainable? |
| **Tren harga** | Apakah pair trending kuat ke satu arah? | Mungkin perlu setel strategi |
| **Tren volume** | Volume trading naik atau turun? | Naik = lebih banyak fee di depan. Turun = mungkin exit. |
| **Besaran IL** | Apa yang bakal lo punya kalo cuma hold? | Jangan ngeboongin diri sendiri soal profitabilitas |

### Tools yang Ngebantu

| Tool | Fungsinya | URL |
|------|-----------|-----|
| **Meteora dApp** | Dashboard posisi lo — sumber kebenaran | app.meteora.ag |
| **Birdeye** | Chart harga token, volume, analytics | birdeye.so |
| **DEX Screener** | Data DEX real-time, pair trending | dexscreener.com |
| **Jupiter** | Harga swap terbaik, data routing | jup.ag |
| **Rugcheck** | Verifikasi keamanan kontrak token | rugcheck.xyz |
| **GMGN** | Tracking memecoin, analisis wallet | gmgn.ai |

Buat LP simpel di pair utama kayak SOL-USDC, Meteora dApp + sesekali cek Birdeye udah cukup.

---

## Keputusan: Kapan Harus Bertindak

### Skenario 1: Harga Mendekati Batas Atas Lo

```
Rentang lo: $180–$220
Harga saat ini: $215 (97.7% rentang, mendekati puncak)
```

**Opsi:**

| Tindakan | Kapan Ngambilnya |
|----------|-----------------|
| **Nggak ngapa-ngapain** | Lo yakin harga bakal tetap di rentang atau balik |
| **Lebarin rentang ke atas** | Lo pengen tetap in range dan terus dapet fee |
| **Pindahin rentang ke atas** | Lo yakin harga udah nemu level baru |
| **Tutup posisi** | Lo pikir tren bakal lanjut kuat dan IL bakal makin parah |

**Kalo lo nggak ngapa-ngapain dan harga naik di atas $220:**
- Posisi lo jadi "out of range"
- Semua aset lo sekarang dalam USDC (lo secara efektif jual semua SOL lo di puncak rentang)
- Lo dapet nol fee sampai harga turun lagi
- Downside lo terlindungi (lo dalam stablecoin)

### Skenario 2: Harga Mendekati Batas Bawah Lo

```
Rentang lo: $180–$220
Harga saat ini: $185 (nyaris di rentang, mendekati bawah)
```

| Tindakan | Kapan Ngambilnya |
|----------|-----------------|
| **Nggak ngapa-ngapain** | Lo percaya sama aset jangka panjang, rela ngumpulin |
| **Lebarin rentang ke bawah** | Lo pengen tetap aktif dan terus dapet |
| **Tutup posisi** | Lo pikir downtrend bakal lanjut dan lo pengen motong rugi |

**Kalo lo nggak ngapa-ngapain dan harga turun di bawah $180:**
- Posisi keluar dari rentang
- Semua aset berubah jadi SOL (lo beli lebih banyak SOL di harga menurun)
- Lo sekarang 100% exposed ke pergerakan harga SOL
- Lo nggak dapet fee

### Skenario 3: Posisi Jauh di Luar Rentang

```
Lo buka di $200, rentang ±10%
Harga sekarang $280 (40% di atas maksimum lo)
Lo udah out of range selama 2 minggu
```

Lo punya tiga pilihan:

1. **Nunggu.** Kalo lo yakin harga bakal balik, posisi lo aktif lagi otomatis pas balik. Nggak perlu transaksi.
2. **Tutup dan buka lagi.** Withdraw, terima IL-nya, dan buka posisi baru di level harga saat ini. Ini mengkristalkan kerugian lo tapi bikin lo dapet fee lagi.
3. **Setel posisi yang ada.** Lebarin atau pindahin rentang lo buat mencakup harga saat ini. Posisi lo langsung aktif lagi.

---

## Kapan Harus Exit: Red Flag

### Hard Exit (Tutup Langsung)

- **Tokennya lagi rug-pull.** Drop 90%+ tiba-tiba, likuiditas menghilang, wallet tim nge-dump. Jangan nunggu. Tutup.
- **Pool ditinggalin.** Volume turun hampir nol, nggak ada trade berhari-hari. Modal lo nggak ngapa-ngapain.
- **Lo butuh duitnya.** Dana LP harusnya "modal yang nggak lo butuhin dalam waktu dekat." Kalo hidup lagi butuh, exit.

### Soft Exit (Pertimbangin Nutup)

- **Fee APR turun di bawah 5% annualized** selama lebih dari sebulan. Lo bisa dapet lebih banyak di tabungan dengan nol risiko.
- **IL udah tumbuh berminggu-minggu dan nggak nunjukin tanda balik.** Tren adalah temen lo, sampai dia bukan.
- **Lo nemu peluang lebih baik.** Modal harus ngalir ke return tertinggi yang disesuaikan risiko.
- **Total volume pool turun bulan ke bulan.** Minat meredup.

---

## Ngukur Profit Sebenernya

Ini skill paling penting dalam LPing, dan kebanyakan orang nggak ngelakuin.

### Framework-nya

Track angka ini buat setiap posisi:

| Metrik | Cara Ngitung |
|--------|-------------|
| **Nilai deposit kotor** | Nilai token yang lo masukin (di harga waktu deposit) |
| **Fee yang didapat** | Akumulasi fee dari dashboard posisi |
| **Nilai withdrawal saat ini** | Nilai token yang bakal lo terima kalo lo tutup sekarang |
| **Nilai HODL** | Nilai kalo lo cuma hold token asli |

### Cuma Dua Angka yang Penting

```
Profit LP = Nilai Withdrawal Saat Ini - Nilai Deposit Kotor

vs

Profit HODL = Nilai HODL - Nilai Deposit Kotor
```

- Kalo Profit LP > Profit HODL → lo menang. LPing nambahin nilai.
- Kalo Profit LP < Profit HODL → lo lebih baik nggak LPing.
- Kalo Profit LP negatif → lo kehilangan duit secara absolut.

### Contoh Realistis

```
Deposit: 0.5 SOL ($100 pas SOL = $200) + 100 USDC = total $200

Setelah 3 bulan:
- SOL sekarang $300 (+50%)
- Posisi berisi: 0.38 SOL + 115 USDC
- Nilai withdrawal saat ini: 0.38 × $300 + 115 = $229
- Nilai HODL: 0.5 × $300 + 100 = $250

Profit LP: $229 - $200 = +$29 (+14.5% dalam 3 bulan)
Profit HODL: $250 - $200 = +$50 (+25% dalam 3 bulan)

Verdict: LPing underperform dibanding hold. IL dari kenaikan SOL 50% ngebiayain lebih mahal daripada fee yang didapat.
```

Ini bukan berarti LPing itu "gagal." Artinya: di market yang trending kuat, strategi LP terkonsentrasi underperform dibanding cuma megang aset yang naik. Tau ini ngebantu lo milih strategi yang cocok buat kondisi market.

---

## Cek Kesehatan LP Bulanan

Sekali sebulan, tanya diri lo:

1. **Apa gue track PnL gue dengan jujur?** (Bandingin HODL, bukan cuma "fee keliatannya oke")
2. **Apa strategi gue masih cocok buat kondisi market saat ini?**
3. **Apa gue ngecek posisi gue di frekuensi yang tepat?** (Terlalu jarang = kecolongan. Terlalu sering = overtrading.)
4. **Apa fee yang gue dapet sepadan sama waktu yang gue habisin?**
5. **Apa gue ngerti KENAPA posisi gue perform kayak gitu?**

Pertanyaan #5 yang paling penting. Posisi profitable yang lo nggak ngerti lebih berbahaya daripada posisi rugi yang lo ngerti — karena yang profitable ngasih lo kepercayaan diri palsu.

---

## Langkah Berikutnya Setelah Dokumen Ini

Lo udah nyelesaiin ceritanya. Dari Budi di terminal bus sampai posisi DLMM pertama lo di Solana.

Ke mana dari sini:

1. **Buka posisi tes kecil** ($20-50). Alamin siklus hidup penuh.
2. **Join komunitas LP Army** (lparmy.com) — Discord LP Meteora tempat LP aktif sharing strategi.
3. **Baca docs resmi** (docs.meteora.ag) — sekarang lo udah punya fondasi konseptual, docs teknis bakal masuk akal.
4. **Track posisi lo dengan jujur** — bandingin HODL, setiap kali.
5. **Scale up bertahap** — seiring lo ngembangin intuisi, bukan sebelumnya.

---

## Satu Konsep Terakhir yang Perlu Diingat

Nggak ada strategi cepet kaya di LPing. Yang ada cuma **return yang disesuaikan risiko.** Pertanyaannya bukan "seberapa banyak yang bisa gue dapet?" — tapi "seberapa banyak risiko yang gue ambil buat dapet itu?"

Kalo seseorang nunjukin screenshot 1000% APR, tanya: *"Berapa impermanent loss-nya? Gimana perbandingan HODL-nya? Ini sustainable atau ini cuma satu hari bagus dalam sebulan kerugian?"*

Yang beneran bikin duit di DeFi bukan yang ngejar angka tertinggi. Mereka yang track PnL dengan jujur, ngerti risiko mereka, dan compounding secara stabil dari waktu ke waktu.

Persis kayak Budi di terminal bus — datang setiap hari, ngatur inventaris, dapet spread. Nggak ada sihir. Cuma matematika dan konsistensi.

---

**Good luck. Mulai kecil. Track dengan jujur. Tetap penasaran.**
