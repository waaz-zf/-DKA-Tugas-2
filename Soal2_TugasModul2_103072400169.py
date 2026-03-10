import numpy as np

print("=== SISTEM DATA INVENTARIS ===")

banyak_barang = int(input("Masukkan jumlah barang: "))

nama_barang = []
kode_barang = []
stok_barang = []
harga_barang = []

for i in range(banyak_barang):
    print("\nData Barang ke-", i+1)

    nb = input("Nama Barang : ")
    kb = input("Kode Barang : ")
    stok = int(input("Jumlah Stok : "))
    harga = float(input("Harga/unit  : "))

    nama_barang.append(nb)
    kode_barang.append(kb)
    stok_barang.append(stok)
    harga_barang.append(harga)

nama_barang = np.array(nama_barang)
kode_barang = np.array(kode_barang)
stok_barang = np.array(stok_barang)
harga_barang = np.array(harga_barang)

nilai_barang = stok_barang * harga_barang

print("\n--- DAFTAR BARANG ---")

for i in range(len(nama_barang)):
    print(
        kode_barang[i],
        "|",
        nama_barang[i],
        "| Stok:", stok_barang[i],
        "| Harga:", harga_barang[i],
        "| Total:", nilai_barang[i]
    )

total_semua = nilai_barang.sum()

print("\nTotal seluruh nilai inventaris:", total_semua)

cari = input("\nCari barang (nama/kode): ")

ada = False

for i in range(len(nama_barang)):
    if cari == nama_barang[i] or cari == kode_barang[i]:
        print("\nBarang ditemukan:")
        print("Nama  :", nama_barang[i])
        print("Kode  :", kode_barang[i])
        print("Jumlah:", stok_barang[i])
        print("Harga :", harga_barang[i])
        print("Total :", nilai_barang[i])
        ada = True
        break

if ada == False:
    print("Barang tidak ditemukan.")