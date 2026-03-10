import numpy as np

print("=== DATA MAHASISWA ===")

jumlah_data = int(input("Berapa data mahasiswa yang ingin dimasukkan? "))

list_nama = []
list_nim = []
list_nilai = []
list_tahun = []

for i in range(jumlah_data):
    print("\nInput Mahasiswa ke-", i+1)

    nm = input("Nama        : ")
    id_mhs = input("NIM         : ")
    nilai_mhs = float(input("Nilai       : "))
    thn_masuk = int(input("Tahun Masuk : "))

    list_nama.append(nm)
    list_nim.append(id_mhs)
    list_nilai.append(nilai_mhs)
    list_tahun.append(thn_masuk)

nama = np.array(list_nama)
nim = np.array(list_nim)
nilai = np.array(list_nilai)
tahun = np.array(list_tahun)

print("\n--- DATA YANG TERSIMPAN ---")
for i in range(len(nama)):
    print("Nama:", nama[i],
          "| NIM:", nim[i],
          "| Nilai:", nilai[i],
          "| Tahun Masuk:", tahun[i])

print("\nStatistik Nilai:")
print("Nilai tertinggi :", nilai.max())
print("Nilai terendah  :", nilai.min())
print("Rata-rata nilai :", round(nilai.mean(),2))

kata = input("\nMasukkan Nama atau NIM yang ingin dicari: ")

ketemu = False

for i in range(len(nama)):
    if kata == nama[i] or kata == nim[i]:
        print("\nData Mahasiswa Ditemukan")
        print("Nama :", nama[i])
        print("NIM  :", nim[i])
        print("Nilai:", nilai[i])
        print("Tahun Masuk:", tahun[i])
        ketemu = True
        break

if ketemu == False:
    print("Data tidak ada.")