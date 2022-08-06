# Program Penyimpan Kontak

from tkinter.tix import InputOnly


def display_kontak(daftar_kontak):
    for kontak in daftar_kontak:
        print("Daftar kontak:")
        print(f"Nama : {kontak['nama1']}")
        print(f"Telepon : {kontak['telepon1']}")
        print(f"Nama : {kontak['nama2']}")
        print(f"Telepon : {kontak['telepon2']}")

def new_kontak():
    nama = input("Nama : ")
    telepon = input("Telepon : ")
    kontak = {
        "nama" : nama,
        "telepon" : telepon
    }
    return kontak 

