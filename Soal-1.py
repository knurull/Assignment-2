# Program Penyimpan Kontak
import function

# List of dictionary
daftar_kontak = []
daftar_kontak.append({
    "nama1" : "Farhan",
    "telepon1" : "08123456789",
    "nama2" : "Joko",
    "telepon2" : "08987654321"
})

# --- Menu ---
while True:
    print("--- Menu ---")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Keluar Program")

    menu = input("Pilih menu : ")

    if menu == "3":
        break
    elif menu == "1":
        function.display_kontak(daftar_kontak)
    elif menu == "2":
        kontak = function.new_kontak()
        daftar_kontak.append(kontak)
    else:
        print("Menu tidak tersedia")

print("Program selesai, sampai jumpa!")