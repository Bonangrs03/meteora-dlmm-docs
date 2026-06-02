# Chapter 9: Concentrated Liquidity — Ide Besarnya

---

## Masalah dengan AMM Tradisional

Inget x × y = k dari Chapter 5? Di sistem itu, likuiditas lo nyebar di SEMUA harga yang mungkin — dari hampir nol sampe hampir tak terhingga.

Nih gambaran buat pool SOL-USDC kita:

```
Rentang harga yang likuiditas lo cover:
├── $0,00001/SOL ← duit lo disini (gak guna)
├── $1/SOL       ← duit lo disini (gak guna)
├── $10/SOL      ← duit lo disini (gak guna)
├── $50/SOL      ← duit lo disini (mungkin gak guna)
├── $200/SOL ← ← ← trading beneran terjadi di SINI
├── $500/SOL     ← duit lo disini (mayoritas gak guna)
├── $5.000/SOL   ← duit lo disini (gak guna)
└── $1.000.000/SOL ← duit lo disini (sepenuhnya gak guna)
```

Mayoritas modal lo duduk di harga yang GAK ADA yang trading. Nganggur. Mubazir. Kayak markirin mobil lo di 100 tempat parkir padahal lo cuma butuh satu.

## Insight-nya

Gimana kalau lo bisa bilang:

> *"Gue cuma mau nyediain likuiditas antara **$180 dan $220 per SOL.** Di dalam range itu, gue fully active. Di luar range itu, gue gak nyediain likuiditas sama sekali."*

Sekarang duit lo terkonsentrasi di tempat trading beneran terjadi. Modal sama, dampak JAUH lebih gede.

Ini namanya **concentrated liquidity.**

## Perbandingan Berdampingan

| | AMM Tradisional (x × y = k) | Concentrated Liquidity |
|---|---|---|
| Rentang harga | $0 sampe ∞ | Lo yang milih (misal, $180–$220) |
| Duit lo duduk dimana | Di mana-mana | Cuma di range yang lo pilih |
| Efisiensi modal | Rendah | Tinggi |
| Penghasilan fee | Terencer di semua harga | Terkonsentrasi di tempat trading terjadi |
| Manajemen dibutuhkan | Gak ada | Lo harus sesuaikan range kalau harga gerak |

## Tradeoff-nya

Concentrated liquidity ngasih lo lebih banyak penghasilan fee per dolar yang disetor — tapi ada konsekuensinya:

```
AMM Tradisional: "Setel dan lupakan." Posisi lo selalu aktif.
                  Membosankan. Return rendah. Aman.

Concentrated:    "Posisi lo cuma aktif di range yang lo pilih."
                  Seru. Return tinggi. Butuh perhatian.
```

Kalau harga SOL gerak keluar dari range $180–$220 lo, likuiditas lo berhenti dapet fee. Lo "out of range." Aset lo nganggur sampe harga balik — atau sampe lo sesuaikan range lo.

## Visualisasinya

Bayangin lo di konser. Panggung adalah tempat aksinya.

- **AMM Tradisional:** Duit lo nyebar di seluruh stadion — tempat parkir, stand konsesi, kursi paling atas, di mana-mana. Sebagian kecil doang yang deket panggung.
- **Concentrated liquidity:** Duit lo dipaketin di baris depan, nempel ke panggung. Dampak maksimum per dolar.

Tapi kalau band-nya pindah ke panggung lain? Lo harus fisik mindahin duit lo ke panggung baru. Itu biaya manajemennya.

## Kenapa Ini Penting (Banget)

Kita kasih angka. Anggap sebuah pool ngelakuin $1 juta volume harian dan ngecharge 0,3% fee ($3.000/hari dalam fee).

| Strategi | Setoran Lo | Porsi Likuiditas Aktif | Fee Harian Didapet |
|----------|-----------|----------------------|-------------------|
| Tradisional (full range) | $10.000 | 0,01% (terencer) | $0,30/hari |
| Concentrated ($180–$220) | $10.000 | 10% (di range itu) | $300/hari |

Setoran sama $10.000. **Perbedaan 1.000× dalam penghasilan fee.** Itu kekuatan konsentrasi.

(Penghasilan dunia nyata gak seekstrim ini karena LP lain juga mengkonsentrasi, tapi prinsipnya berlaku.)

## Uniswap V3: Pelopornya

Concentrated liquidity diperkenalkan ke DeFi oleh Uniswap V3 di Mei 2021. Ini ngubah segalanya. Tiba-tiba, LP bisa jauh lebih capital-efficient.

Tapi Uniswap V3 dibangun di Ethereum, dengan semua masalah biaya gas yang kita bahas di Chapter 8. Manajemen aktif secara teori mungkin tapi secara praktik mahal.

## Kesempatan Solana

Di Solana, concentrated liquidity bisa beneran *dikelola secara aktif* oleh orang biasa. Lo bisa sesuaikan range lo harian, klaim fee per jam, compound terus-menerus — semua cuma sepersekian sen per aksi.

Ini kenapa Meteora DLMM ada. Dia ngambil concentrated liquidity dan ngedorong lebih jauh — dengan desain yang dioptimasi buat kecepatan Solana.

## Satu Konsep yang Harus Diingat

> **Concentrated liquidity** = alih-alih nyebar duit lo di semua harga, lo milih rentang harga spesifik di mana modal lo aktif. Ini bikin duit lo kerja lebih keras — tapi maksa lo buat ngelola posisi kalau harga gerak keluar dari range lo.

---

*Selanjutnya: Meteora DLMM — gimana dia ngimplementasiin concentrated liquidity secara berbeda dari yang lain? Apa itu "bin" dan kenapa itu penting?*
