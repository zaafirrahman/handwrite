# Handwrite Tool
## Alat bantu buat bikin laprak tultang dll.

- Liat dulu contoh hasil jadinya di file 'demo.png', silaken lanjut klo tertarik

Cara menyiapkan (Mungkin bakal susah dan agak lama, tapi cuma sekali doang, sisanya ntar ez)
- Install python 3 dulu di laptop kalian
- Download repo ini terus extract di folder kalian
- Tulis seluruh karakter keyboard kalian di atas kertas putih secara jelas dan ukurannya seragam (termasuk shifted caharacter)
- Scan tultang kalian secara jelas, dekat, dan ga blur, terus save pake filter magic color (buat yang berwarna) atau no shadow (buat warna item) kalau kalian pakai camscanner
- Terserah mau bikin berapa set (kelompok karakter), semakin banyak semakin bagus karna semakin beragam jenis font kalian
- Masukin ke folder 'raw-font'
- Buka file 'font-editor.psd' di folder font-scanned > letters terus masukin hasil scan kalian
- Zoom sampe cuma keliatan 1 karakter doang di worksheet psd
- Atur sampe karakter berada di tengah guideline (nyesuain posisi masing-masing huruf misal 'g' ekornya rada kebawahin dikit sama 'h' ujung atasnya rada naikin dikit, dsb)
- Save as dalam format .png per karakternya lalu dinamain berdasarkan urutan ASCII (sesuain aja sama contoh yang udah ada) lalu simpan ke masing-masing folder 'set' di folder 'letters'

Cara menggunakan
- Copas atau ketik apapun yang kalian mau tulis ke dalam file 'draft.txt' jangan lupa disave
- Buka Command Prompt atau PowerShell, sesuain direktori dimana repo ini kalian save, abistu ketik 'create.py'
- Buka file 'sheet.html' dan simsalabim, ketikan berubah jadi tultang seketika
- Tinggal ss abistu merge sama lembaran2 lainnya, tinggal submit deh
