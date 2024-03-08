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

    def sort(self, key='nomor_kamar', order='ascending'):
        if order not in ['ascending', 'descending']:
            print("Order harus 'ascending' atau 'descending'.")
            return
        if key not in ['nomor_kamar', 'harga_per_malam']:
            print("Key harus 'nomor_kamar' atau 'harga_per_malam'.")
            return
        self.head = self._quick_sort(self.head, key, order)

    def _quick_sort(self, start, key, order):
        if not start or not start.next:
            return start

        pivot_prev = start
        pivot = start
        current = start.next

        while current:
            if (order == 'ascending' and getattr(current, key) < getattr(pivot, key)) or \
               (order == 'descending' and getattr(current, key) > getattr(pivot, key)):
                pivot_prev.next = current.next
                current.next = pivot
                pivot = current
                current = pivot_prev.next
            else:
                pivot_prev = current
                current = current.next

        if pivot != start:
            temp = start
            while temp.next != pivot:
                temp = temp.next
            temp.next = None

            left = self._quick_sort(start, key, order)
            right = self._quick_sort(pivot.next, key, order)

            pivot.next = right
            if left:
                temp = left
                while temp.next:
                    temp = temp.next
                temp.next = pivot
                return left
            else:
                return pivot
        else:
            pivot.next = self._quick_sort(pivot.next, key, order)
            return pivot


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


def menu():
    print("====| pilihan Menu |====")
    print("1. Tambah Kamar di Awal")
    print("2. Tambah Kamar di Akhir")
    print("3. Tambah Kamar di Tengah")
    print("4. Hapus Kamar")
    print("5. Info Kamar")
    print("6. Semua Kamar")
    print("7. Sorting")
    print("8. Keluar")
    return input("Pilih menu: ")


print("=== Program Manajemen Kamar Hotel ===")
hotel = Hotel()
while True:
    pilihan = menu ()
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
        key = input("Pilih kunci untuk sorting ('nomor_kamar' atau 'harga_per_malam'): ")
        order = input("Pilih urutan sorting ('ascending' atau 'descending'): ")
        hotel.kamar.sort(key=key, order=order)
        print("Kamar berhasil diurutkan.")
    elif pilihan == '8':
        print("Terima kasih, sampai jumpa!")
        break
