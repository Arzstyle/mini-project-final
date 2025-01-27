def format_rupiah(amount):
    return f"Rp{amount:,.0f}".replace(",", ".")

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

neraca_keuangan = [
    {"Kategori": "Kas di tangan",            "Jumlah": 18000000},
    {"Kategori": "Piutang Usaha",            "Jumlah": 10500000},
    {"Kategori": "Hutang Pajak",             "Jumlah": 12000000},
    {"Kategori": "Hutang Bank",              "Jumlah": 50000000},
    {"Kategori": "Aktiva Tetap",             "Jumlah": 300000000},
    {"Kategori": "Deposito",                 "Jumlah": 20000000},
    {"Kategori": "Peralatan Kantor",         "Jumlah": 15000000},
    {"Kategori": "Investasi Jangka Panjang", "Jumlah": 100000000},
    {"Kategori": "Hutang Hipotik",           "Jumlah": 25000000},
    {"Kategori": "Jumlah Modal",             "Jumlah": 550000000},
]


sorted_neraca = merge_sort(neraca_keuangan, key="Jumlah")

print("Kategori                        Jumlah")
print("---------------------------------------------")
for item in sorted_neraca:
    print(f"{item['Kategori']:30} {format_rupiah(item['Jumlah'])}")