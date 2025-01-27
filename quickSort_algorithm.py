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
