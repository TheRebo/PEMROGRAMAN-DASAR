menu = {
    "1": ("Nasi Goreng", 15000, 5),
    "2": ("Mie Ayam", 15000, 0),
    "3": ("Soto", 15000, 3),
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
        kode_list = [k.strip() for k in input("\nPilih menu (nomor, pisahkan dengan koma): ").split(",")]
        if any(k not in menu for k in kode_list) or len(set(kode_list)) != len(kode_list):
            print("Menu tidak valid (nomor tidak ada atau doble).")
            continue

        daftar_nama = ", ".join(menu[k][0] for k in kode_list)
        try:
            jumlah_list = [int(j) for j in input(f"Jumlah ({daftar_nama}): ").split(",")]
            if len(jumlah_list) != len(kode_list) or any(j <= 0 for j in jumlah_list):
                raise ValueError
        except ValueError:
            print("Jumlah tidak valid (harus bilangan > 0 dan sebanyak menu yang dipilih).")
            continue

        return dict(zip(kode_list, jumlah_list))

def sistem_memeriksa_stok(pesanan):
    return [menu[k][0] for k, j in pesanan.items() if menu[k][2] < j]

def menghitung_total_pembayaran(pesanan):
    return sum(menu[k][1] * j for k, j in pesanan.items())

def sistem_menampilkan_ringkasan(pesanan, total):
    print("\n=== RINGKASAN PESANAN ===")
    for k, j in pesanan.items():
        nama, harga, _ = menu[k]
        print(f"{nama:<12} {j} x Rp{harga:,} = Rp{harga * j:,}")
    print(f"{'TOTAL':<12} Rp{total:,}")

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
        pesanan = pengguna_memilih_menu()
        habis = sistem_memeriksa_stok(pesanan)
        if not habis:
            break
        print(f"Stok tidak cukup: {', '.join(habis)}. Silakan memilih ulang.")

    total = menghitung_total_pembayaran(pesanan)

    sistem_menampilkan_ringkasan(pesanan, total)

    while True:
        uang = pengguna_memasukkan_uang()

        if sistem_memvalidasi_pembayaran(uang, total):
            kembalian = uang - total
            if kembalian > 0:
                print(f"Kembalian: Rp{kembalian:,}")

            for k, j in pesanan.items():
                nama, harga, stok = menu[k]
                menu[k] = (nama, harga, stok - j)

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
