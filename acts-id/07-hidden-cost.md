# Chapter 7: Biaya Tersembunyi — Impermanent Loss

---

## Balik ke Budi

Inget risiko inventaris Budi dari Chapter 3? Dia beli voucher pulsa di Rp 9.800, terus provider turunin harga ke Rp 8.000. Inventarisnya tiba-tiba nilainya lebih rendah.

LPing punya risiko yang persis sama. Tapi di DeFi, ada nama spesifiknya: **impermanent loss.**

## Apa Itu Impermanent Loss?

Impermanent loss terjadi ketika harga aset yang lo setor berubah relatif satu sama lain — dan perubahan itu bikin posisi lo bernilai *lebih rendah* dibanding kalau lo cuma hold asetnya secara terpisah.

Biar konkret.

## Skenarionya

Lo setor ke pool SOL-USDC:

| Setoran Lo | Jumlah | Nilai USD |
|-----------|--------|----------|
| SOL | 1 SOL | $200 (di harga $200/SOL) |
| USDC | 200 USDC | $200 |
| **Total** | | **$400** |

Pool berfungsi. Trade terjadi. Lo dapet sejumlah fee.

Terus harga SOL naik 2× lipat. Sekarang $400 per SOL.

Kalau lo cuma hold 1 SOL dan 200 USDC lo secara terpisah:

| Aset | Jumlah | Nilai Baru |
|------|--------|-----------|
| SOL | 1 SOL | $400 |
| USDC | 200 USDC | $200 |
| **Total kalau hold** | | **$600** |

$600. Lo untung $200.

Tapi lo gak hold terpisah — lo masukin aset lo ke pool. Kita liat apa yang terjadi di dalam pool.

## Yang Dilakukan Pool Ketika SOL Naik 2×

Rumus pool adalah x × y = k. Ketika harga pasar SOL naik 2×, trader arbitrase buru-buru masuk. Mereka beli SOL dari pool (yang masih dihargain sekitar $200) dan jual di pasar terbuka di $400, ngantongin selisihnya.

Pembelian ini ngerus SOL dari pool dan nambahin USDC. Setelah arbitrase selesai, pool rebalancing:

| Aset Pool | Sebelum (SOL di $200) | Setelah (SOL di $400) |
|----------|---------------------|---------------------|
| SOL di pool | 10 SOL (dari semua LP) | ~7,07 SOL |
| USDC di pool | 2.000 USDC | ~2.828 USDC |

Bagian lo (anggap 10%):

| Bagian Lo | Jumlah | Nilai di $400/SOL |
|----------|--------|------------------|
| SOL | 0,707 SOL | $282,80 |
| USDC | 282,80 USDC | $282,80 |
| **Total dari pool** | | **$565,60** |

Bandingin:

| Skenario | Nilai |
|----------|------|
| Kalau lo cuma HOLD | $600,00 |
| Kalau lo LP | $565,60 |
| **Impermanent Loss** | **$34,40 (5,7%)** |

Lo kehilangan $34,40 dibanding cuma hold. Itu impermanent loss.

## Kenapa Disebut "Impermanent"?

Kerugiannya disebut *impermanent* karena belum terkunci sampai lo tarik. Kalau harga SOL balik ke $200, bagian pool lo balik ke 1 SOL + 200 USDC. Kerugiannya hilang. Sementara doang.

Tapi kalau lo tarik saat harga masih $400? Kerugiannya jadi **permanen.**

## Matematika yang Kejam

Nih skala impermanent loss terhadap perubahan harga:

| Perubahan Harga | Impermanent Loss |
|----------------|------------------|
| 1,25× (naik 25%) | ~0,6% |
| 1,5× (naik 50%) | ~2,0% |
| 2× (naik 100%) | ~5,7% |
| 3× (naik 200%) | ~13,4% |
| 5× (naik 400%) | ~25,5% |
| 10× (naik 900%) | ~42,5% |

Makin gede harga bergerak — ke arah MANAPUN — makin banyak yang lo hilangin dibanding cuma hold.

## Model Mentalnya

Anggap pool AMM sebagai kekuatan yang **melawan perubahan harga.**

Ketika harga SOL naik, pool jual SOL (ke trader arbitrase) buat dorong harga balik turun.
Ketika harga SOL turun, pool beli SOL buat dorong harga balik naik.

Sebagai LP, lo ada di sisi yang salah dari setiap pergerakan harga besar. Pool secara otomatis "beli mahal dan jual murah" dari perspektif lo. Itu sumber impermanent loss.

## Apa Fee Bisa Nutupin?

Ya — itu inti permainannya.

Kalau lo dapet cukup fee untuk ngalahin impermanent loss, lo untung. Kalau nggak, mendingan lo cuma hold.

| Skenario | Fee Didapet | Impermanent Loss | Hasil Bersih |
|----------|-----------|------------------|-------------|
| Pair stabil (USDC-USDT) | 5% APR | ~0% | ✅ Untung |
| Volatilitas sedang (SOL-USDC) | 30% APR | 5,7% IL | ✅ Untung |
| Volatilitas ekstrim (memecoin baru) | 200% APR | 42,5% IL | ❌ Rugi bersih |

Ini kenapa LP berpengalaman lebih milih:
- **Pair stabil** (IL rendah, fee stabil)
- **Pair volume tinggi** (banyak fee buat nutup IL)
- **Time horizon pendek** (lebih kecil kemungkinan pergerakan harga besar)

## Satu Konsep yang Harus Diingat

> **Impermanent loss** = selisih antara nilai aset lo di dalam pool vs nilai aset kalau lo cuma hold. Dia membesar seiring harga bergerak menjauh dari titik masuk lo. Fee harus ngalahin ini buat lo untung.

Ini konsep paling penting yang harus lo ngerti sebelum jadi LP. Kalau lo cuma inget satu hal dari seluruh dokumen ini, inget ini: **LPing bukan duit gratis. Lo lagi jual volatilitas dan dibayar pake fee.**

---

*Selanjutnya: Kita udah ngomongin pool secara abstrak. Sekarang kita liat blockchain spesifik — kenapa Solana? Kenapa bukan Ethereum? Apa bedanya teknologi dasarnya?*
