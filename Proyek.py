harga_buku = 15000
jumlah_buku = 3
harga_pulpen = 5000
jumlah_pulpen = 2

total_buku = harga_buku * jumlah_buku
total_pulpen = harga_pulpen * jumlah_pulpen
total_belanja = total_buku + total_pulpen

if total_belanja >= 50000:
    besarnya_diskon = total_belanja * 0.1
else:
    besarnya_diskon = 0

total_bayar = total_belanja - besarnya_diskon

print("Total harga buku:", total_buku)
print("Total harga pulpen:", total_pulpen)
print("Total belanja sebelum diskon:", total_belanja)
print("Besarnya diskon:", besarnya_diskon)
print("Total yang harus dibayar Andi:", total_bayar)
