# Chapter 6: Dari Mana Uangnya Datang?

---

## Pool Butuh Barang

Pool AMM yang kita bangun di Chapter 5 isinya 10 SOL dan 2.000 USDC. Inventaris itu datang dari suatu tempat.

Di dunia Budi, Budi pake uang sendiri buat beli inventaris. Dia keluarin Rp 5.000.000 dari tabungan buat beli voucher pulsa. Dia nanggung semua risiko, dan dia ngantongin semua untung.

Tapi pool crypto beda. Inventarisnya gak datang dari satu orang. Datangnya dari **siapa aja yang mau ikut.**

## Liquidity Provider (LP)

**Liquidity provider** (disingkat LP) adalah orang yang nyetor asetnya ke pool AMM supaya pool punya inventaris buat trading.

> **LP** = lo, nyetor token lo ke pool supaya AMM bisa berfungsi sebagai market maker.

Imbalannya, lo dapet bagian dari fee setiap trade yang terjadi di pool itu.

## Gimana Cara Kerjanya, Step by Step

Anggap lo punya 1 SOL dan 200 USDC. Lo liat ada pool SOL-USDC.

**Step 1: Lo setor.**
Lo masukin 1 SOL dan 200 USDC ke pool. Pool sekarang punya inventaris lebih banyak.

**Step 2: Pool pake aset lo.**
Trader datang dan trading di pool. Setiap trade bayar fee kecil (biasanya 0,3% atau kurang).

**Step 3: Lo dapet bagian lo.**
Kalau setoran lo mewakili 10% dari total pool, lo dapet 10% dari semua fee yang terkumpul.

**Step 4: Lo bisa tarik kapan aja.**
Kalau lo mau duit lo balik, lo tarik bagian lo dari pool — aset awal lo plus fee yang udah lo kumpulin.

## Contoh Nyata

Kita lacak pake angka:

| Event | Status Pool | Bagian Lo |
|-------|------------|----------|
| Pool mulai | 10 SOL + 2.000 USDC | — |
| Lo setor | 1 SOL + 200 USDC | 1/11 = 9,09% dari pool |
| Pool sekarang | 11 SOL + 2.200 USDC | — |
| 100 trade terjadi | Fee terkumpul: ~10 USDC | Bagian lo: ~0,91 USDC |
| Lo tarik | Lo dapet balik bagian lo | 1 SOL + ~200,91 USDC |

Lo dapet ~0,91 USDC cuma karena ninggalin aset di pool. Bukan jumlah yang mengubah hidup, tapi bayangin ini jalan setahun dengan ribuan trade per hari.

## Kenapa Ini Bagus Buat Pool?

Pool butuh kedalaman. Pool dengan 10 SOL gak bisa nanganin trade 5 SOL tanpa price impact gede (inget Chapter 5). Pool dengan 1.000 SOL bisa nanganin trade itu dengan mulus.

Lebih banyak LP → pool lebih dalam → slippage lebih kecil → pengalaman trading lebih enak → lebih banyak trader → lebih banyak fee → LP makin senang.

Ini siklus positif. Seluruh ekosistem DeFi jalan di atas ini.

## Kenapa Ada yang Mau Ngelakuin Ini?

Tiga alasan:

| Alasan | Penjelasan |
|--------|-----------|
| **Dapet fee pasif** | Aset lo kerja buat lo sementara lo tidur. Kayak bunga di rekening bank, tapi yield-nya datang dari trading fee, bukan dari pinjaman. |
| **Dukung project yang lo percaya** | LP awal yang nyediain likuiditas bikin token baru bisa ditradingin. Tanpa LP, token baru gak punya pasar. |
| **Diversifikasi portofolio** | Daripada cuma hold SOL, lo bisa manfaatin itu buat dapet yield tambahan. |

## Deal-nya: Apa yang Lo Kasih vs Apa yang Lo Dapet

| Lo KASIH | Lo DAPET |
|----------|---------|
| Aset lo (SOL, USDC, dll.) | Bagian dari semua trading fee |
| Kemampuan lo buat jual kapan aja (aset terkunci di pool) | Hak buat tarik kapan aja (gak ada masa lockup) |
| Lo nanggung risiko inventaris | Lo dapet yield pasif |

Baris ketiga — "lo nanggung risiko inventaris" — cukup penting sampe pantes dapet chapter sendiri.

---

*Selanjutnya: Biaya tersembunyi jadi LP. Kenapa "tinggal setor dan dapet" bukan gambaran lengkapnya.*
