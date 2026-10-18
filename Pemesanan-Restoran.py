menu = {
    "1": ("Nasi Goreng", 15000, 5),
    "2": ("Mie Ayam", 15000, 0),
    "3": ("Soto Banjar", 15000, 3),
    "4": ("Es Teh", 5000, 10),
}

antrean_terakhir = 0

def buat_nomor_antrean():
    global antrean_terakhir
    antrean_terakhir += 1
    return antrean_terakhir

def sistem_menampilkan_menu():
    print("\n=== menu RESTORAN ===")
    for kode, (nama, harga, stok) in menu.items():
        print(f"{kode}. {nama:<12} Rp{harga:,}  (stok: {stok})")

def pengguna_memilih_menu():
    while True:
        kode = input("\nPilih menu (nomor): ").strip()
        if kode not in menu:
            print("Menu tidak ditemukan.")
            continue
        try:
            jumlah = int(input("Jumlah: "))
            if jumlah <= 0:
                raise ValueError
        except ValueError:
            print("Jumlah tidak valid.")
            continue
        return kode, jumlah

def sistem_memeriksa_stok(kode, jumlah):
    return menu[kode][2] >= jumlah

def menghitung_total_pembayaran(kode, jumlah):
    return menu[kode][1] * jumlah

def pengguna_memasukkan_uang():
    while True:
        try:
            uang = int(input("Masukkan uang: Rp"))
            if uang < 0:
                raise ValueError
            return uang
        except ValueError:
            print("Jumlah uang tidak valid.")

def sistem_memvalidasi_pembayaran(uang, total):
    return uang >= total

def main():
    print("START")

    sistem_menampilkan_menu()

    while True:
        kode, jumlah = pengguna_memilih_menu()
        if sistem_memeriksa_stok(kode, jumlah):
            break
        print("Stok habis, silakan memilih menu lain.")

    total = menghitung_total_pembayaran(kode, jumlah)
    print(f"\nTotal pembayaran: Rp{total:,}")

    while True:
        uang = pengguna_memasukkan_uang()

        if sistem_memvalidasi_pembayaran(uang, total):
            kembalian = uang - total
            if kembalian > 0:
                print(f"Kembalian: Rp{kembalian:,}")
            nama, harga, stok = menu[kode]
            menu[kode] = (nama, harga, stok - jumlah)
            nomor_antrean = buat_nomor_antrean()
            print(f"Nomor antrean Anda: {nomor_antrean}")
            print("Penjual sedang menyiapkan pesanan...")
            print(f"Pesanan nomor {nomor_antrean} sudah siap, silakan diambil.")
            print("Status pemesanan: SELESAI")
            break

        print(f"Pembayaran gagal: uang kurang Rp{total - uang:,}. Ulangi atau batal")
        pilihan = ""
        while pilihan not in ("ulangi", "batal"):
            pilihan = input("Pilihan (ulangi/batal): ").strip().lower()

        if pilihan == "batal":
            print("Pesanan dibatalkan")
            break

    print("END")

if __name__ == "__main__":
    main()
