# Data perjalanan
jarak = 100
konsumsi = 40
sisa_bensin = 1.5
harga_bensin = 10000

# Menghitung jarak pulang-pergi
total_jarak = jarak * 2

# Menghitung kebutuhan bahan bakar
total_bensin = total_jarak / konsumsi

# Menghitung bahan bakar yang harus dibeli
bensin_beli = max(0, total_bensin - sisa_bensin)

# Menghitung total biaya
total_biaya = bensin_beli * harga_bensin

# Menampilkan hasil
print("Total jarak:", total_jarak, "km")
print("Kebutuhan bensin:", total_bensin, "liter")
print("Bensin yang dibeli:", bensin_beli, "liter")
print("Total biaya: Rp", total_biaya)
