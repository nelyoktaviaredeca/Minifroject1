class Hotel:
    def __init__(self):
        self.kamar = {}

    def tambah_kamar(self, nomor_kamar, kapasitas, harga_per_malam, dipesan=False):
        if nomor_kamar not in self.kamar:
            self.kamar[nomor_kamar] = {"kapasitas": kapasitas, "harga_per_malam": harga_per_malam, "dipesan": dipesan}
            print(f"Kamar nomor {nomor_kamar} berhasil ditambahkan.")
        else:
            print(f"Kamar nomor {nomor_kamar} sudah ada dalam sistem.")

    def hapus_kamar(self, nomor_kamar):
        if nomor_kamar in self.kamar:
            del self.kamar[nomor_kamar]
            print(f"Kamar nomor {nomor_kamar} berhasil dihapus.")
        else:
            print(f"Kamar nomor {nomor_kamar} tidak ditemukan dalam sistem.")

    def update_kamar(self, nomor_kamar, **kwargs):
        if nomor_kamar in self.kamar:
            for key, value in kwargs.items():
                if key in self.kamar[nomor_kamar]:
                    self.kamar[nomor_kamar][key] = value
                    print(f"{key} kamar nomor {nomor_kamar} berhasil diupdate.")
                else:
                    print(f"{key} bukan merupakan field yang valid untuk kamar.")
        else:
            print(f"Kamar nomor {nomor_kamar} tidak ditemukan dalam sistem.")

    def info_kamar(self, nomor_kamar):
        if nomor_kamar in self.kamar:
            info_kamar = self.kamar[nomor_kamar]
            print(f"Informasi Kamar {nomor_kamar}:")
            print(f"Kapasitas: {info_kamar['kapasitas']}")
            print(f"Harga per Malam: {info_kamar['harga_per_malam']}")
            print(f"Status: {'Terpesan' if info_kamar['dipesan'] else 'Tersedia'}")
        else:
            print(f"Kamar nomor {nomor_kamar} tidak ditemukan dalam sistem.")

    def semua_kamar(self):
        if self.kamar:
            print("Daftar Kamar:")
            for nomor_kamar, info_kamar in self.kamar.items():
                print(f"Nomor Kamar: {nomor_kamar}, Kapasitas: {info_kamar['kapasitas']}, Harga per Malam: {info_kamar['harga_per_malam']}, Status: {'Terpesan' if info_kamar['dipesan'] else 'Tersedia'}")
        else:
            print("Belum ada kamar yang ditambahkan.")

# Fungsi untuk meng-handle input dari pengguna
def menu():
    print("====| pilihan Menu |====")
    print("1. Tambah Kamar")
    print("2. Hapus Kamar")
    print("3. Update Kamar")
    print("4. Info Kamar")
    print("5. Semua Kamar")
    print("6. Keluar")
    return input("Pilih menu: ")

# Judul Program
print("=== Program Manajemen Kamar Hotel ===")

# Contoh penggunaan
hotel = Hotel()
while True:
    pilihan = menu()
    if pilihan == '1':
        try:
            nomor = int(input("Nomor Kamar: "))
            kapasitas = int(input("Kapasitas: "))
            harga = int(input("Harga per Malam: "))
            hotel.tambah_kamar(nomor, kapasitas, harga)
        except ValueError:
            print("Masukkan harus berupa bilangan bulat.")
    elif pilihan == '2':
        try:
            nomor = int(input("Nomor Kamar yang akan dihapus: "))
            hotel.hapus_kamar(nomor)
        except ValueError:
            print("Masukkan harus berupa bilangan bulat.")
    elif pilihan == '3':
        try:
            nomor = int(input("Nomor Kamar yang akan diupdate: "))
            kapasitas = int(input("Kapasitas baru: "))
            harga = int(input("Harga per Malam baru: "))
            hotel.update_kamar(nomor, kapasitas=kapasitas, harga_per_malam=harga)
        except ValueError:
            print("Masukkan harus berupa bilangan bulat.")
    elif pilihan == '4':
        try:
            nomor = int(input("Nomor Kamar: "))
            hotel.info_kamar(nomor)
        except ValueError:
            print("Masukkan harus berupa bilangan bulat.")
    elif pilihan == '5':
        hotel.semua_kamar()
    elif pilihan == '6':
        print("Terima kasih, sampai jumpa!")
        break
    else:
        print("Menu tidak valid. Silakan pilih menu yang benar.")
