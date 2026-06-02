# Bab 4: Gimana Kalau Middleman-nya Adalah Program Komputer?

---

## Budi Punya Masalah

Masih inget Budi dari Bab 3? Dia lumayan sukses. Tapi dia capek banget. Berdiri di terminal bus 14 jam sehari. Dia harus hadir secara fisik buat setiap transaksi.

Suatu malam, Budi punya ide: *"Gimana kalau gue bikin program komputer yang ngerjain kerjaan gue?"*

Dia nelpon ponakannya, seorang programmer.

"Dengerin," kata Budi. "Gue butuh program yang ngegantiin gue. Programnya harus ngelakuin tepat tiga hal:"

1. **Megang inventori** — programnya harus megang pulsa dan duit, kayak yang gue lakuin.
2. **Nentuin harga** — programnya harus tau harga beli dan jual yang harus dipasang.
3. **Eksekusi transaksi** — ketika ada yang pengen trading, programnya jalanin otomatis.

Ponakannya mikir sebentar. "Yang pertama dan ketiga gampang. Yang susah itu nomor 2 — gimana programnya tau harga apa yang harus dipasang?"

## Satu Aturan yang Dibutuhin Program

Budi ngejelasin instingnya: *"Ketika banyak orang beli dari gue, gue pelan-pelan naikin harga. Ketika banyak orang jual ke gue, gue pelan-pelan turunin harga. Gue gak mikir — gue cuma ngerasain keramaiannya."*

Ponakannya nerjemahin ini ke logika kode:

```
Kalau seseorang BELI dari program:
    → Inventori aset di program TURUN
    → Jadi program harus NAIKIN harga sedikit

Kalau seseorang JUAL ke program:
    → Inventori aset di program NAIK
    → Jadi program harus TURUNIN harga sedikit
```

Ini masuk akal. Kalau semua orang pengen beli pulsa dari mesin, pulsa jadi makin langka di dalam mesin. Harga naik. Kalau semua orang jual pulsa ke mesin, mesin kebanjiran pulsa. Harga turun.

**Ini persis cara kerja pasar keuangan beneran.** Saham Apple naik ketika lebih banyak yang pengen beli daripada jual. Turun ketika lebih banyak yang pengen jual daripada beli. Mesin cuma memformalkan ini ke dalam kode.

## Automated Market Maker (AMM)

Program ini — robot yang megang inventori, nentuin harga secara algoritmik, dan trading otomatis — namanya **Automated Market Maker,** atau **AMM.**

> **AMM** = program komputer yang bertindak sebagai market maker, pake matematika (bukan penilaian manusia) buat nentuin harga.

Alih-alih Budi berdiri di terminal bikin keputusan berdasarkan feeling, kita punya program yang jalan 24/7, memproses transaksi instan, gak pernah capek, gak pernah bikin kesalahan emosional.

## Perbedaan Kunci: Siapa yang Nentuin Harga?

| Pasar Tradisional (Bursa Saham) | Automated Market Maker (DeFi) |
|-------------------------------------|-------------------------------|
| Pembeli dan penjual pasang order | Gak ada order. Cuma pool aset. |
| Order book yang mencocokkan | Formula yang ngitung harga. |
| Harga = di mana supply ketemu demand | Harga = kata formula, berdasarkan seberapa banyak yang ada di pool. |
| Butuh banyak partisipan buat berfungsi | Bisa jalan cuma dengan SATU penyedia aset. |

Poin terakhir ini revolusioner. Exchange tradisional butuh banyak pembeli DAN banyak penjual buat berfungsi. Tanpa cukup partisipan, order book kosong dan trading macet.

AMM bisa jalan dengan satu orang aja yang deposit aset. Formulanya nanganin price discovery. Artinya **lo bisa bikin pasar yang berfungsi buat aset apapun, kapan aja, dengan setup yang hampir gak ada.**

## Tradeoff-nya

Tentu aja, Budi si manusia punya kelebihan:

| Budi (Manusia) | AMM (Program) |
|--------------|---------------|
| Bisa nyesuaiin sama berita dan kejadian | Cuma ngikutin formulanya |
| Bisa nolak transaksi mencurigakan | Trading sama siapa aja, selalu |
| Capek, butuh tidur | Jalan selamanya |
| Bikin kesalahan karena feeling | Nol kesalahan penilaian |
| Gak bisa scale di luar satu lokasi | Bisa ngelayani seluruh internet |

Buat crypto, yang global, 24/7, dan murni digital, model AMM itu pas banget. Gak tidur. Gak ada batasan negara. Gak ada hari sakit.

## Di Mana Kita Sekarang

Sejauh ini, kita udah bangun:

```
Bab 1: Likuiditas = kemudahan trading
Bab 2: Market maker nyediain likuiditas, untung dari spread
Bab 3: Profit = spread × volume − risiko inventori
Bab 4: AMM adalah program komputer yang ngerjain kerjaan market maker
```

AMM adalah jembatan antara terminal bus Budi dan dunia DeFi. Tapi kita masih belum jawab pertanyaan utamanya:

**Formula apa yang sebenernya dipake AMM buat nentuin harga?**

Itu Bab 5.

---

*Selanjutnya: Matematika di dalam mesin. Tenang aja — ini lebih simpel dari yang lo kira.*
