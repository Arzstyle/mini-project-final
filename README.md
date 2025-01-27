# **Analisis dan Implementasi Algoritma Pengurutan: Merge Sort dan Quick Sort**

## **Deskripsi Proyek**
Proyek ini bertujuan untuk mengimplementasikan dan menganalisis dua algoritma pengurutan populer, yaitu **Merge Sort** dan **Quick Sort**. Studi kasus yang diangkat adalah pengurutan data berbasis numerik dan kategori pada konteks tertentu, seperti penjualan tahunan dan neraca keuangan.

---

### Kelompok 5
- M. Akbar Rizky Saputra
- M. Zulfan Mulana aldiansyah
- M. Sinar Agusta
- Arizieq Iskandar

**Kelas:** TI23A

**Mata Kuliah:** Kompleksitas Algoritma  
**Dosen Pengampu:** Zaaenal Alamsyah, M.Kom

---
 ## **MODULE TAMBAHAN**
 Catatan: Pastikan library prettytable terinstall di Visual Studio Code untuk Python, agar output table bisa terlihat.

 **Contoh:** 
``` 
pip install prettytable
```


## **Algoritma yang Digunakan**

### **1. Merge Sort**
#### **Deskripsi**
Merge Sort adalah algoritma pengurutan berbasis **Divide and Conquer** yang membagi data menjadi bagian-bagian kecil, mengurutkan masing-masing bagian secara rekursif, dan menggabungkannya kembali untuk menghasilkan urutan yang teratur.

#### **Implementasi**
Studi kasus menggunakan **Merge Sort** untuk mengurutkan neraca keuangan berdasarkan jumlah aset.

```python
def merge_sort(data, key):
    if len(data) <= 1:
        return data

    middle = len(data) // 2
    left_half = merge_sort(data[:middle], key)
    right_half = merge_sort(data[middle:], key)

    return merge(left_half, right_half, key)

def merge(left, right, key):
    result = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index][key] <= right[right_index][key]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result

# Studi Kasus
neraca_keuangan = [
    {"Kategori": "Kas di tangan", "Jumlah": 18000000},
    {"Kategori": "Piutang Usaha", "Jumlah": 10500000},
    {"Kategori": "Hutang Pajak", "Jumlah": 12000000},
    {"Kategori": "Hutang Bank", "Jumlah": 50000000},
    {"Kategori": "Aktiva Tetap", "Jumlah": 300000000},
    {"Kategori": "Deposito", "Jumlah": 20000000},
    {"Kategori": "Peralatan Kantor", "Jumlah": 15000000},
    {"Kategori": "Investasi Jangka Panjang", "Jumlah": 100000000},
    {"Kategori": "Hutang Hipotik", "Jumlah": 25000000},
    {"Kategori": "Jumlah Modal", "Jumlah": 550000000},
]

sorted_neraca = merge_sort(neraca_keuangan, key="Jumlah")

print("Kategori                        Jumlah")
print("---------------------------------------------")
for item in sorted_neraca:
    print(f"{item['Kategori']:30} Rp{item['Jumlah']:,}")
```

**Contoh Output:**

| Kategori                     | Jumlah          |
|------------------------------|-----------------|
| Piutang Usaha               | Rp10.500.000    |
| Hutang Pajak                | Rp12.000.000    |
| Peralatan Kantor            | Rp15.000.000    |
| Kas di tangan               | Rp18.000.000    |
| Deposito                    | Rp20.000.000    |
| Hutang Hipotik              | Rp25.000.000    |
| Hutang Bank                 | Rp50.000.000    |
| Investasi Jangka Panjang    | Rp100.000.000   |
| Aktiva Tetap                | Rp300.000.000   |
| Jumlah Modal                | Rp550.000.000   |


---


### **2. Quick Sort**
#### **Deskripsi:**
Quick Sort adalah algoritma pengurutan berbasis Divide and Conquer yang bekerja dengan memilih elemen pivot, mempartisi data menjadi dua bagian berdasarkan nilai pivot, dan mengurutkan setiap bagian secara rekursif.

**Karakteristik Utama:**
  - Kompleksitas waktu terbaik dan rata-rata: 
    𝑂 (𝑛 log 𝑛)
  - Kompleksitas waktu terburuk: 
    𝑂 (𝑛2) , jika pivot dipilih buruk.
  - Tidak stabil, sehingga elemen dengan nilai yang sama bisa bertukar posisi.

#### **Implementasi Studi Kasus**
Studi kasus ini menggunakan Quick Sort untuk mengurutkan data penjualan tahunan berdasarkan total penjualan.

``` python
# STUDI KASUS DATA PENJUALAN TAHUNAN TOKO

def format_rupiah(amount):
    return f"Rp{amount:,.0f}".replace(",", ".")

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = []  
    right = []  

    for element in arr[1:]:
        if element["total_penjualan"] < pivot["total_penjualan"]:
            left.append(element)
        else:
            right.append(element)

    return quick_sort(left) + [pivot] + quick_sort(right)

data_penjualan = [
    {"tgl": "3/12/2019",    "no_order": 1,     "pembeli": "UD Makmur",            "total_penjualan": 2000000},
    {"tgl": "6/12/2019",    "no_order": 2,     "pembeli": "Toko Laris Manis",     "total_penjualan": 6000000},
    {"tgl": "10/12/2019",   "no_order": 3,     "pembeli": "Toko Hidup Maju",      "total_penjualan": 5500000},
    {"tgl": "20/12/2019",   "no_order": 4,     "pembeli": "Pusat Grosir",         "total_penjualan": 6700000},
    {"tgl": "26/12/2019",   "no_order": 5,     "pembeli": "Toko Sejahtera",       "total_penjualan": 10400000},
    {"tgl": "2/1/2020",     "no_order": 6,     "pembeli": "Toko Bersama",         "total_penjualan": 3000000},
    {"tgl": "5/1/2020",     "no_order": 7,     "pembeli": "Warung Kita",          "total_penjualan": 8000000},
    {"tgl": "15/1/2020",    "no_order": 8,     "pembeli": "Minimarket Sejahtera", "total_penjualan": 5000000},
    {"tgl": "20/1/2020",    "no_order": 9,     "pembeli": "Supermart Modern",     "total_penjualan": 4500000},
    {"tgl": "25/1/2020",    "no_order": 10,    "pembeli": "Pasar Tradisional",    "total_penjualan": 1000000},
]

sorted_data = quick_sort(data_penjualan)

print(f"{'Tanggal':<12} {'No Order':<10} {'Pembeli':<25} {'Total Penjualan':<15}")
print("-" * 70)
for data in sorted_data:
    print(f"{data['tgl']:<12} {data['no_order']:<10} {data['pembeli']:<25} {format_rupiah(data['total_penjualan']):<15}")

```

**Contoh Output:**

| Tanggal      | No Order | Pembeli                   | Total Penjualan   |
|--------------|----------|---------------------------|-------------------|
| 25/1/2020    | 10       | Pasar Tradisional         | Rp1.000.000       |
| 3/12/2019    | 1        | UD Makmur                 | Rp2.000.000       |
| 2/1/2020     | 6        | Toko Bersama              | Rp3.000.000       |
| 20/1/2020    | 9        | Supermart Modern          | Rp4.500.000       |
| 15/1/2020    | 8        | Minimarket Sejahtera      | Rp5.000.000       |
| 10/12/2019   | 3        | Toko Hidup Maju           | Rp5.500.000       |
| 6/12/2019    | 2        | Toko Laris Manis          | Rp6.000.000       |
| 20/12/2019   | 4        | Pusat Grosir              | Rp6.700.000       |
| 5/1/2020     | 7        | Warung Kita               | Rp8.000.000       |
| 26/12/2019   | 5        | Toko Sejahtera            | Rp10.400.000      |


---


### **Penjelasan**
  - **A. Merge Sort**
    Konsep: Membagi data menjadi dua bagian hingga data menjadi unit terkecil, mengurutkan unit tersebut, lalu menggabungkannya kembali.
      - Fungsi Utama:
        merge_sort(): Membagi data.
        merge(): Menggabungkan data yang sudah diurutkan.
        
  - **B. Quick Sort**
    Konsep: Memilih elemen acuan (pivot) dari data, memisahkan elemen lebih kecil atau lebih besar dari pivot, dan menggabungkan hasil rekursifnya.
      - Fungsi Utama:
        quick_sort(): Rekursi berdasarkan pivot.


---


### **Kelebihan dan Kekurangan**
  - **A. Merge Sort**
      - Kelebihan:
          - Stabil: Mempertahankan urutan relatif elemen yang sama.
          - Cocok untuk data besar karena kompleksitas waktu terburuk selalu 𝑂 (𝑛 log 𝑛 )
      - Kekurangan:
          - Membutuhkan ruang tambahan karena menggunakan array baru untuk penggabungan.
          - Kurang efisien untuk data kecil.

  - **B. Quick Sort**
      - Kelebihan:
          - Tidak membutuhkan ruang tambahan yang signifikan.
          - Sangat cepat untuk data kecil hingga menengah dalam kasus rata-rata.
      - Kekurangan:
          - Tidak stabil: Urutan relatif elemen dengan nilai sama tidak selalu dipertahankan.
          - Kompleksitas waktu terburuk 𝑂 (𝑛2) jika pivot dipilih buruk.



## Perbandingan Algoritma
| Kriteria         | Merge Sort                      | Quick Sort                      |
|------------------|---------------------------------|---------------------------------|
| **Metode**       | Divide and Conquer             | Divide and Conquer             |
| **Kompleksitas** | O(n log n)                     | O(n log n) rata-rata; O(n²) terburuk |
| **Stabilitas**   | Stabil                         | Tidak Stabil                   |
| **Penggunaan Memori** | Memerlukan memori tambahan     | Tidak memerlukan memori tambahan |
| **Kecepatan**    | Konsisten pada dataset besar   | Cepat untuk dataset kecil      |


## **Kesimpulan**
  - Dalam pengolahan data keuangan dan penjualan, metode pengurutan yang digunakan memainkan peran penting untuk efisiensi dan akurasi analisis. Pada tabel neraca keuangan, algoritma Merge Sort digunakan karena kemampuannya dalam menangani data yang besar dan kompleks, seperti aset, kewajiban, dan modal, yang membutuhkan pengurutan stabil serta pengelompokan terstruktur. Dengan Merge Sort, data dapat diproses secara efisien tanpa mengorbankan integritas informasi, sehingga menghasilkan gambaran yang akurat tentang posisi keuangan perusahaan.
  - Di sisi lain, pada tabel penjualan, algoritma Quick Sort diterapkan karena efisiensinya dalam mengurutkan data yang lebih dinamis, seperti tanggal transaksi, total penjualan, dan nama pembeli. Quick Sort lebih unggul dalam situasi di mana data sering berubah dan membutuhkan pengurutan cepat untuk analisis langsung. Sebagai contoh, identifikasi pembeli dengan penjualan tertinggi (Toko Sejahtera) dan pembeli dengan kontribusi terkecil (Pasar Tradisional) dapat dilakukan dengan mudah menggunakan pendekatan ini.
  - Secara keseluruhan, penggunaan Merge Sort pada tabel neraca keuangan memastikan pengolahan data yang terstruktur dan stabil, sedangkan Quick Sort pada tabel penjualan memungkinkan pengurutan data yang cepat dan responsif. Kombinasi kedua algoritma ini mendukung perusahaan dalam menganalisis data keuangan dan operasional secara optimal untuk pengambilan keputusan strategis.







