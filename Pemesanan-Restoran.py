import random

NAMA_RESTORAN = "Restoran Lorem Ipsum"
LEBAR = 46

menu = {
    1: {"nama": "Nasi Goreng", "harga": 20000, "stok": 5},
    2: {"nama": "Mie Ayam",    "harga": 15000, "stok": 0},
    3: {"nama": "Sate Ayam",   "harga": 25000, "stok": 3},
    4: {"nama": "Es Teh",      "harga": 5000,  "stok": 10},
}

keranjang = {}
batal = False
berhasil = False
total = 0

def rupiah(angka):
    """20000 -> Rp20.000"""
    return "Rp" + f"{angka:,}".replace(",", ".")

def garis(simbol="-"):
    print(simbol * LEBAR)

def tampilkan_menu():
    print()
    garis("=")
    print(NAMA_RESTORAN.center(LEBAR))
    garis("=")
    print(f"{'No':<4}{'Menu':<16}{'Harga':>12}{'Stok':>10}")
    garis()
    for nomor, item in menu.items():
        stok = "HABIS" if item["stok"] == 0 else str(item["stok"])
        print(f"{nomor:<4}{item['nama']:<16}{rupiah(item['harga']):>12}{stok:>10}")
    garis()

def hitung_total():
    jumlah_total = 0
    for nomor, jumlah in keranjang.items():
        jumlah_total += menu[nomor]["harga"] * jumlah
    return jumlah_total

def tampilkan_keranjang(judul, pakai_nomor=False):
    print()
    garis()
    print(judul.center(LEBAR))
    garis()
    for nomor, jumlah in keranjang.items():
        baris = f"{menu[nomor]['nama']} x{jumlah}"
        if pakai_nomor:
            baris = f"{nomor}. " + baris
        subtotal = rupiah(menu[nomor]["harga"] * jumlah)
        print(f"{baris:<30}{subtotal:>16}")
    garis()
    print(f"{'TOTAL':<30}{rupiah(hitung_total()):>16}")
    garis()

print("START")
tampilkan_menu()

while True:
    print("\nKetik nomor menu untuk memesan.")
    print("Perintah lain: 'menu', 'keranjang', 'hapus', 'selesai' (bayar), 'batal'")
    pilih = input("Pilihan: ").strip().lower()

    if pilih == "batal":
        batal = True
        break

    if pilih == "menu":
        tampilkan_menu()
        continue

    if pilih == "keranjang":
        if len(keranjang) == 0:
            print("Keranjang masih kosong.")
        else:
            tampilkan_keranjang("ISI KERANJANG")
        continue

    if pilih == "hapus":
        if len(keranjang) == 0:
            print("Keranjang masih kosong, tidak ada yang bisa dihapus.")
            continue
        tampilkan_keranjang("ISI KERANJANG", pakai_nomor=True)
        hapus = input("Nomor menu yang dihapus: ").strip()
        if hapus.isdigit() and int(hapus) in keranjang:
            nama = menu[int(hapus)]["nama"]
            del keranjang[int(hapus)]
            print(f"- {nama} dihapus dari keranjang.")
        else:
            print("Nomor tersebut tidak ada di keranjang.")
        continue

    if pilih == "selesai":
        if len(keranjang) == 0:
            print("Keranjang masih kosong, silakan pilih menu dulu.")
            continue
        break

    if not pilih.isdigit() or int(pilih) not in menu:
        print("Nomor menu tidak ada di daftar, coba lagi.")
        continue

    nomor = int(pilih)
    item = menu[nomor]

    if item["stok"] == 0:
        print(f"Maaf, {item['nama']} sedang habis. Silakan pilih menu lain.")
        continue

    jumlah = input(f"Jumlah {item['nama']}: ").strip()
    if not jumlah.isdigit() or int(jumlah) == 0:
        print("Jumlah harus berupa angka lebih dari 0.")
        continue
    jumlah = int(jumlah)

    sisa = item["stok"] - keranjang.get(nomor, 0)
    if jumlah > sisa:
        print(f"Maaf, stok {item['nama']} tidak cukup. Sisa yang bisa dipesan: {sisa}.")
        continue

    keranjang[nomor] = keranjang.get(nomor, 0) + jumlah
    print(f"+ {item['nama']} x{jumlah} masuk keranjang.")
    print(f"  Total sementara: {rupiah(hitung_total())}")

if not batal:
    total = hitung_total()
    tampilkan_keranjang("RINGKASAN PESANAN")

bayar = 0
while not batal and not berhasil:
    masukan = input("\nMasukkan uang pembayaran (angka saja): ").strip()

    if masukan.isdigit() and int(masukan) >= total:
        bayar = int(masukan)
        berhasil = True
    else:
        if masukan.isdigit():
            print(f"Pembayaran gagal: uang kurang {rupiah(total - int(masukan))}.")
        else:
            print("Pembayaran gagal: masukkan nominal berupa angka.")

        pilihan = ""
        while pilihan != "ulangi" and pilihan != "batal":
            pilihan = input("Pilih (ulangi/batal): ").strip().lower()
        if pilihan == "batal":
            batal = True

if berhasil:
    for nomor, jumlah in keranjang.items():
        menu[nomor]["stok"] -= jumlah

    status = "diproses"
    nomor_antrean = random.randint(1, 99)
    kode_pengambilan = random.randint(1000, 9999)

    print(f"\nPembayaran berhasil! Kembalian: {rupiah(bayar - total)}")
    print("Menyimpan pesanan...")
    print(f"Nomor antrean    : {nomor_antrean}")
    print(f"Status pesanan   : {status}")
    print("Penjual sedang menyiapkan pesanan...")

    status = "siap diambil"
    print(f"Notifikasi       : Pesanan nomor {nomor_antrean} {status}!")
    print(f"Kode pengambilan : {kode_pengambilan}")
    print("Silakan tunjukkan kode pengambilan kepada penjual.")

    status = "selesai"
    print(f"Status pesanan   : {status}")
    print("\nTerima kasih, selamat menikmati!")
else:
    print("\nPesanan dibatalkan. Sampai jumpa!")

print("\nEND")
