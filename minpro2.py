# Sistem Pendataan Daftar Warisan Budaya

# Data awal (dictionary dengan ID sebagai key)
daftar_budaya = {
    1: {"nama": "Batik", "asal": "Yogyakarta", "jenis": "Benda", "tahun": "2009"},
    2: {"nama": "Wayang", "asal": "Jawa Tengah", "jenis": "Tak Benda", "tahun": "2008"},
    3: {"nama": "Angklung", "asal": "Jawa Barat", "jenis": "Tak Benda", "tahun": "2010"}
}

# Akun login
users = {
    "admin": {"password": "admin123", "role": "Admin"},
    "pengunjung": {"password": "guest123", "role": "Pengunjung"}
}

# Fungsi tampil data
def tampilkan_data():
    if not daftar_budaya:
        print("\nBelum ada data yang tersimpan.")
    else:
        print("\n=== Daftar Warisan Budaya ===")
        for id_budaya, data in daftar_budaya.items():
            print(f"{id_budaya}. {data['nama']} - {data['asal']} - {data['jenis']} - {data['tahun']}")

# Fungsi tambah data
def tambah_data():
    try:
        id_baru = max(daftar_budaya.keys()) + 1 if daftar_budaya else 1

        # Validasi Nama
        while True:
            nama = input("Masukkan nama budaya: ")
            if nama.replace(" ", "").isalpha():
                break
            print("Nama tidak valid! Harap masukkan huruf.")

        # Validasi Asal
        while True:
            asal = input("Masukkan asal budaya: ")
            if asal.replace(" ", "").isalpha():
                break
            print("Asal tidak valid! Harap masukkan huruf.")

        # Validasi Jenis
        while True:
            jenis = input("Masukkan jenis budaya (Benda/Tak Benda): ")
            if jenis.lower() in ["benda", "tak benda"]:
                jenis = "Benda" if jenis.lower() == "benda" else "Tak Benda"
                break
            print("Jenis tidak valid! Hanya boleh 'Benda' atau 'Tak Benda'.")

        # Validasi Tahun
        while True:
            tahun = input("Masukkan tahun: ")
            if tahun.isdigit():
                break
            print("Tahun tidak valid! Harap masukkan angka.")

        daftar_budaya[id_baru] = {"nama": nama, "asal": asal, "jenis": jenis, "tahun": tahun}
        print("\nData berhasil ditambahkan.")

    except Exception as e:
        print("Terjadi kesalahan:", e)

# Fungsi ubah data
def ubah_data():
    tampilkan_data()
    try:
        id_edit = int(input("Masukkan ID data yang ingin diubah: "))
        if id_edit not in daftar_budaya:
            print("ID tidak ditemukan!")
            return

        # Validasi Nama
        while True:
            nama = input("Masukkan nama baru: ")
            if nama.replace(" ", "").isalpha():
                break
            print("Nama tidak valid! Masukkan hanya huruf.")

        # Validasi Asal
        while True:
            asal = input("Masukkan asal baru: ")
            if asal.replace(" ", "").isalpha():
                break
            print("Asal tidak valid! Masukkan hanya huruf.")

        # Validasi Jenis
        while True:
            jenis = input("Masukkan jenis baru (Benda/Tak Benda): ")
            if jenis.lower() in ["benda", "tak benda"]:
                jenis = "Benda" if jenis.lower() == "benda" else "Tak Benda"
                break
            print("Jenis tidak valid! Hanya boleh 'Benda' atau 'Tak Benda'.")

        # Validasi Tahun
        while True:
            tahun = input("Masukkan tahun baru: ")
            if tahun.isdigit():
                break
            print("Tahun tidak valid! Masukkan  angka.")

        daftar_budaya[id_edit] = {"nama": nama, "asal": asal, "jenis": jenis, "tahun": tahun}
        print("\nData berhasil diubah.")

    except ValueError:
        print("Input ID harus berupa angka!")

# Fungsi hapus data
def hapus_data():
    tampilkan_data()
    try:
        id_hapus = int(input("Masukkan ID data yang ingin dihapus: "))
        if id_hapus not in daftar_budaya:
            print("ID tidak ditemukan!")
            return
        del daftar_budaya[id_hapus]
        print("\nData berhasil dihapus.")
    except ValueError:
        print("Input ID harus berupa angka!")

# Sistem login
print("=== LOGIN SISTEM ===")
username = input("Username: ")
password = input("Password: ")

if username in users and users[username]["password"] == password:
    role = users[username]["role"]
    print(f"\nLogin berhasil! Anda masuk sebagai {role}.")

    if role == "Admin":
        while True:
            print("\n=== Menu Admin ===")
            print("1. Lihat Daftar Budaya")
            print("2. Tambah Data Budaya")
            print("3. Ubah Data Budaya")
            print("4. Hapus Data Budaya")
            print("5. Keluar")

            pilihan = input("Pilih menu (1-5): ")

            if pilihan == "1":
                tampilkan_data()
            elif pilihan == "2":
                tambah_data()
            elif pilihan == "3":
                ubah_data()
            elif pilihan == "4":
                hapus_data()
            elif pilihan == "5":
                print("Keluar dari sistem.")
                break
            else:
                print("Pilihan tidak valid!")

    elif role == "Pengunjung":
        while True:
            print("\n=== Menu Pengunjung ===")
            print("1. Lihat Daftar Budaya")
            print("2. Keluar")

            pilihan = input("Pilih menu (1-2): ")

            if pilihan == "1":
                tampilkan_data()
            elif pilihan == "2":
                print("Keluar dari sistem.")
                break
            else:
                print("Pilihan tidak valid!")

else:
    print("Login gagal! Username atau password salah.")