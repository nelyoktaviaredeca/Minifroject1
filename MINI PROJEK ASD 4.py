import math

class Node:
    def __init__(self, nomor_kamar, kapasitas, harga_per_malam, dipesan=False):
        self.nomor_kamar = nomor_kamar
        self.kapasitas = kapasitas
        self.harga_per_malam = harga_per_malam
        self.dipesan = dipesan
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def tambah_node_di_awal(self, nomor_kamar, kapasitas, harga_per_malam, dipesan=False):
        new_node = Node(nomor_kamar, kapasitas, harga_per_malam, dipesan)
        new_node.next = self.head
        self.head = new_node

    def tambah_node_di_akhir(self, nomor_kamar, kapasitas, harga_per_malam, dipesan=False):
        if not self.head:
            self.head = Node(nomor_kamar, kapasitas, harga_per_malam, dipesan)
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = Node(nomor_kamar, kapasitas, harga_per_malam, dipesan)

    def tambah_node_di_tengah(self, prev_node, nomor_kamar, kapasitas, harga_per_malam, dipesan=False):
        if not prev_node:
            print("Node sebelumnya tidak boleh kosong.")
            return
        new_node = Node(nomor_kamar, kapasitas, harga_per_malam, dipesan)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def hapus_node(self, nomor_kamar):
        temp = self.head
        if temp is not None:
            if temp.nomor_kamar == nomor_kamar:
                self.head = temp.next
                temp = None
                print("Kamar berhasil dihapus")  # Pesan kamar berhasil dihapus
                return
        while temp is not None:
            if temp.nomor_kamar == nomor_kamar:
                break
            prev = temp
            temp = temp.next
        if temp is None:
            print("Nomor kamar tidak ditemukan.")
            return
        prev.next = temp.next
        temp = None

    def jump_search(self, nomor_kamar=None, harga_permalam=None):
        n = self.count_nodes()
        step = int(math.sqrt(n))
        prev = None
        current = self.head

        # Mencari kamar berdasarkan nomor kamar
        if nomor_kamar is not None:
            while current and current.nomor_kamar < nomor_kamar:
                prev = current
                for _ in range(step):
                    if current:
                        prev = current
                        current = current.next
            if current and current.nomor_kamar == nomor_kamar:
                return current
            else:
                return None
        
        # Mencari kamar berdasarkan harga per malam
        elif harga_permalam is not None:
            while current and current.harga_per_malam < harga_permalam:
                prev = current
                for _ in range(step):
                    if current:
                        prev = current
                        current = current.next
            if current and current.harga_per_malam == harga_permalam:
                return current
            else:
                return None
        else:
            return None

    def count_nodes(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    def get_node_at_index(self, index):
        temp = self.head
        count = 0
        while temp:
            if count == index:
                return temp
            temp = temp.next
            count += 1
        return None


class Hotel:
    def __init__(self):
        self.kamar = LinkedList()

    def tambah_kamar(self, nomor_kamar, kapasitas, harga_per_malam, dipesan=False, posisi='akhir'):
        if posisi == 'awal':
            self.kamar.tambah_node_di_awal(nomor_kamar, kapasitas, harga_per_malam, dipesan)
        elif posisi == 'akhir':
            self.kamar.tambah_node_di_akhir(nomor_kamar, kapasitas, harga_per_malam, dipesan)
        else:
            prev_node = self.kamar.head
            while prev_node:
                if prev_node.nomor_kamar == posisi:
                    break
                prev_node = prev_node.next
            self.kamar.tambah_node_di_tengah(prev_node, nomor_kamar, kapasitas, harga_per_malam, dipesan)
        print("Kamar berhasil ditambahkan")  # Pesan kamar berhasil ditambahkan

    def hapus_kamar(self, nomor_kamar):
        self.kamar.hapus_node(nomor_kamar)

    def info_kamar(self, nomor_kamar):
        temp = self.kamar.head
        while temp:
            if temp.nomor_kamar == nomor_kamar:
                print(f"Informasi Kamar {nomor_kamar}:")
                print(f"Kapasitas: {temp.kapasitas}")
                print(f"Harga per Malam: {temp.harga_per_malam}")
                print(f"Status: {'Terpesan' if temp.dipesan else 'Tersedia'}")
                return
            temp = temp.next
        print(f"Kamar nomor {nomor_kamar} tidak ditemukan dalam sistem.")

    def semua_kamar(self):
        temp = self.kamar.head
        if temp is None:
            print("Belum ada kamar yang ditambahkan.")
            return
        print("Daftar Kamar:")
        while temp:
            print(f"Nomor Kamar: {temp.nomor_kamar}, Kapasitas: {temp.kapasitas}, Harga per Malam: {temp.harga_per_malam}, Status: {'Terpesan' if temp.dipesan else 'Tersedia'}")
            temp = temp.next

    def cari_kamar(self):
        print("Pilih kriteria pencarian:")
        print("1. Nomor Kamar")
        print("2. Harga per Malam")
        pilihan = input("Masukkan pilihan (1/2): ")
        if pilihan == '1':
            nomor_kamar = int(input("Masukkan nomor kamar yang ingin dicari: "))
            result = self.kamar.jump_search(nomor_kamar=nomor_kamar)
            if result:
                print(f"Kamar dengan nomor {nomor_kamar} ditemukan.")
                print(f"Kapasitas: {result.kapasitas}")
                print(f"Harga per Malam: {result.harga_per_malam}")
                print(f"Status: {'Terpesan' if result.dipesan else 'Tersedia'}")
            else:
                print(f"Kamar dengan nomor {nomor_kamar} tidak ditemukan.")
        elif pilihan == '2':
            harga_permalam = int(input("Masukkan harga per malam yang ingin dicari: "))
            result = self.kamar.jump_search(harga_permalam=harga_permalam)
            if result:
                print(f"Kamar dengan harga per malam {harga_permalam} ditemukan.")
                print(f"Nomor Kamar: {result.nomor_kamar}")
                print(f"Kapasitas: {result.kapasitas}")
                print(f"Status: {'Terpesan' if result.dipesan else 'Tersedia'}")
            else:
                print(f"Kamar dengan harga per malam {harga_permalam} tidak ditemukan.")
        else:
            print("Pilihan tidak valid.")

def menu():
    print("====| pilihan Menu |====")
    print("1. Tambah Kamar di Awal")
    print("2. Tambah Kamar di Akhir")
    print("3. Tambah Kamar di Tengah")
    print("4. Hapus Kamar")
    print("5. Info Kamar")
    print("6. Semua Kamar")
    print("7. Cari Kamar")
    print("8. Keluar")
    return input("Pilih menu: ")


print("=== Program Manajemen Kamar Hotel ===")
hotel = Hotel()
while True:
    pilihan = menu()
    if pilihan == '1':
        try:
            nomor = int(input("Nomor Kamar: "))
            kapasitas = int(input("Kapasitas: "))
            harga = int(input("Harga per Malam: "))
            hotel.tambah_kamar(nomor, kapasitas, harga, posisi='awal')
        except ValueError:
            print("Masukkan harus berupa bilangan bulat.")
    elif pilihan == '2':
        try:
            nomor = int(input("Nomor Kamar: "))
            kapasitas = int(input("Kapasitas: "))
            harga = int(input("Harga per Malam: "))
            hotel.tambah_kamar(nomor, kapasitas, harga)
        except ValueError:
            print("Masukkan harus berupa bilangan bulat.")
    elif pilihan == '3':
        try:
            nomor = int(input("Nomor Kamar: "))
            kapasitas = int(input("Kapasitas: "))
            harga = int(input("Harga per Malam: "))
            posisi = int(input("Masukkan nomor kamar sebelumnya: "))
            hotel.tambah_kamar(nomor, kapasitas, harga, posisi)
        except ValueError:
            print("Masukkan harus berupa bilangan bulat.")
    elif pilihan == '4':
        try:
            nomor = int(input("Nomor Kamar yang akan dihapus: "))
            hotel.hapus_kamar(nomor)
        except ValueError:
            print("Masukkan harus berupa bilangan bulat.")
    elif pilihan == '5':
        try:
            nomor = int(input("Nomor Kamar: "))
            hotel.info_kamar(nomor)
        except ValueError:
            print("Masukkan harus berupa bilangan bulat.")
    elif pilihan == '6':
        hotel.semua_kamar()
    elif pilihan == '7':
        hotel.cari_kamar()
    elif pilihan == '8':
        print("Terima kasih, sampai jumpa!")
        break
