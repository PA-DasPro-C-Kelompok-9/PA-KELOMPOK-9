from prettytable import PrettyTable 
import json 
import pwinput 
import os 
os.system("cls")


#prettytable 
tabel_data = PrettyTable()
tabel_data.field_names = ["No","Kode", "Layanan", "Harga/Jam", "Status"]


#file json untuk menyimpan data klien
pathDataPengguna = r"C:\users\lenovo\Desktop\ddp praktikum\dataakunpengguna.json"
with open(pathDataPengguna, "r") as data:
    klien = json.loads(data.read())  

#file json untuk menyimpan data layanan 
pathLayanan =   r"C:\users\lenovo\Desktop\ddp praktikum\datalayanan.json"
with open(pathLayanan, "r") as data:
    data = json.loads(data.read())

#variabel untuk mengakses dictionary pada file json
username = klien.get("Nama")
pasword = klien.get("Password")
saldo = klien.get("E-Money")


#fungsi untuk menyimpan data setelah diubah 
def simpan():
    with open("produk.json", "w") as sn:
        json.dump(data, sn, indent=4)

#login admin
def login_admin():
    print("\n+---------------------------------------------------+")
    print("|                   LOGIN AKUN ADMIN                  |")
    print("+-----------------------------------------------------+")
    while True:
        try:
            nama = input("Username : ")
            pw = pwinput.pwinput("Password : ")
            if nama.lower(

            ) == "bitajihantania" and pw == "09":
                print("\n                === LOGIN BERHASIL ===          \n")
                return menu_admin()
                
            else:
                print("\nLOGIN ANDA GAGAL COBA LAGI ATAU KEMBALI")
                while True :
                    balik = input("Apakah anda ingin ke menu utama? (y/t) : ")
                    if balik == "y":
                        main_program()
                        break
                    elif balik == "t":
                        login_admin()
                        break
                    else :
                        print("\nPILIHAN TIDAK TERSEDIA")      
        except :
            print("\nPERHATIKAN INPUT")

#login klien
def login_klien():
    print("\n+-----------------------------------------------------+")
    print("|                 LOGIN AKUN KLIEN                      |")
    print("+-------------------------------------------------------+")
    while True :
        try : 
            nama = input("Masukkan username Anda : ")
            password = pwinput.pwinput("Masukkan password Anda : ")
            global cari
            cari = username.index(nama)
            if nama.lower() == username[cari] and password == pasword[cari]:
                os.system("cls")
                print("\n                 === LOGIN BERHASIL ===                \n")
                menu_klien2()
                break
            elif nama.lower( )== username[cari] and password != pasword[cari]:
                print("\nPASSWORD YANG ANDA INPUT SALAH")
                print("MOHON UNTUK COBA LAGI\n")
                Lanjut = input(" Apakah anda ingin kembali ke menu utama? (y/t) : ")
                if Lanjut == "y":
                    print()
                    menu_klien1()     
                elif Lanjut == "t":
                    print()
                    login_klien()
                    return
                else :
                    print("\nHANYA KETIK y/t")
                    login_klien()
                    return
            elif nama.lower() != username[cari] and password == pasword[cari]:
                print("\nUSERNAME YANG ANDA INPUT SALAH")
                print("\nMOHON UNTUK COBA LAGI\n")
                Lanjut = input("Apakah anda ingin kembali ke menu utama? (y/t) : ")
                if Lanjut == "y":
                    print()
                    menu_klien1()     
                elif Lanjut == "t":
                    login_klien()
                else :
                    print("\nHANYA KETIK y/t")
                    login_klien()
                    return
        except ValueError:
            print("\n USERNAME BELUM TERDAFTAR")
            print("MOHON UNTUK COBA LAGI\n")
            Lanjut = input("Apakah anda ingin kembali ke menu utama? (y/t) : ")
            if Lanjut == "y":
                print()
                menu_klien1()     
            elif Lanjut == "t":
                login_klien()
            else :
                print("\nHANYA KETIK y/t")
                login_klien()
            return

#registrasi klien
def registrasi_klien():
    print("\n+-----------------------------------------------------+")
    print("|              REGISTRASI AKUN KLIEN                    |")
    print("+-------------------------------------------------------+")
    while True :
        try:
            nama = input("Masukkan username yang ingin dibuat : ")
            if nama.lower() == "":
                print("INPUT HARUS DI ISI")
        
            elif all(x.isalpha() for x in nama):
                if nama.lower() in klien ["Nama"]:
                    print("MAAF USERNAME SUDAH ADA, SILAHKAN BUAT USERNAME LAGI!\n")
                    while True :
                        print("+-----------------------------------------------------+")
                        print("|1. Login Akun                                        |")
                        print("|2. Registrasi Akun Baru                              |")
                        print("+-----------------------------------------------------+")
                        pilihan = input("Masukan pilihan anda : ")
                        if pilihan == "1":
                            login_klien()
                            break
                        elif pilihan == "2":
                            print("\nSILAHKAN REGISTRASI USERNAME YANG BARU")
                            registrasi_klien()
                        else :
                            print("\n-> PILIHAN TIDAK ADA\n")

                else:
                    password = pwinput.pwinput("Masukan password yang ingin dibuat : ")
                    if password == "":
                        print("-> INPUT HARUS DI ISI!")
                
                    elif all(x.isnumeric() or x.isalpha() for x in password):
                        saldo_emoney = 0
                        saldo.append(saldo_emoney)
                        username.append(nama)
                        pasword.append(password)
                        if len(str(password)) > 3:
                                print("PASSWORD TIDAK BOLEH LEBIH DARI 3 ANGKA")
                                return
                                                        
                                                        
                        with open(pathDataPengguna, "w") as add_klien:
                            json.dump(klien, add_klien, indent=4)   
                        print("\n            === REGISTRASI AKUN BERHASIL ===          \n")
                        login_klien()
                        break
                    
                        
            else :
                print("USERNAME HARUS BERUPA HURUF!")
                    
        except :
            print("PERHATIKAN INPUT!\n")


# CRUD (admin)

#  create
def create():
    read()
    print("\n      === MENAMBAHKAN DATA LAYANAN BARU ===    \n")
    
    kode = get_kode()
    tambah = get_layanan()
    harga = get_harga()
    status = "ONLINE"
    

    data["Kode"].append(kode)
    data["Layanan"].append(tambah)
    data["Harga"].append(harga)
    data["Status"].append(status)
    
    read()
    simpan()
    print("\n        === DATA BERHASIL DITAMBAHKAN ===      \n")

def get_kode():
    while True:
        kode = input(">> Kode = ")
        if kode in data["Kode"]:
            print("\n JANGAN MENGISI KODE YANG SAMA!\n")
        elif len(kode) == 3 and kode.isdigit():
            return kode
        else:
            print("\n KODE HARUS 3 DIGIT ANGKA!\n")

def get_layanan():
    while True:
        tambah = input(" Layanan : ").capitalize()
        if tambah in data["Layanan"]:
            print("\n LAYANAN SUDAH ADA, TAMBAH LAYANAN LAIN\n")
        else:
            return tambah

def get_harga():
    while True:
        try:
            harga = int(input(" Harga : Rp "))
            if harga <= 0:
                print("\n  HARGA HARUS LEBIH DARI 0\n")
            elif harga > 100000000:
                print("\n HARGA TIDAK BOLEH LEBIH DARI 100000000\n")
            else:
                return harga
        except ValueError:
            print("\n MASUKAN ANGKA\n")
            
# read
def read():
    no = 1
    tabel_data.clear_rows()
    for i in range(len(data["Layanan"])):
        tabel_data.add_row(
            [
                no,
                (data["Kode"][i]),
                (data["Layanan"][i]),
                "Rp." + str(data["Harga"][i]),
                data["Status"][i],
            ]
        )
        no += 1
        simpan()

    print(tabel_data)

#update
def update():
    print("\n          === MEMPERBARUI DATA LAYANAN ===          \n")
    read()
    
    kode_to_update = input("Masukkan kode yang ingin diperbarui : ")
    
    if kode_to_update not in data["Kode"]:
        print("\n KODE TIDAK ADA PADA DATA \n")
        return
    
    cari_n = data["Kode"].index(kode_to_update)
    
    while True:
        nm = input("\n Apakah anda ingin memperbarui layanan? (y/t) : ")
        if nm == "y":
            nub = input(" Masukan layanan baru : ").capitalize()
            if nub in data["Layanan"]:
                print("\n LAYANAN SUDAH ADA")
                
            elif all(x.isalpha() or x.isspace() for x in nub) and len(nub) <= 40:  
                data.get("Layanan")[cari_n] = nub
                print("\n          === LAYANAN BERHASIL DIPERBARUI === \n")
                break
            else:
                print("\n ISI LAYANAN DENGAN HURUF!")
                print("NAMA TIDAK BOLEH LEBIH DARI 40 HURUF!\n")
        elif nm == "t":
            break
        else:
            print("\nPILIHAN TIDAK ADA")


    simpan()
    read()
    print("\n         --- DATA BERHASIL DIPERBARUI ---        \n")

    while True:
        hm = input("\n Apakah anda ingin memperbarui harga ? (y/t) : ")
        if hm == "y":
            while True :
                try :
                    hp_b = int(input(" Masukkan harga baru : Rp. "))
                    if hp_b < 0:
                        print("\n HARGA TIDAK BOLEH KURANG DARI 0")
                    elif hp_b == 0:
                        print("\n-> HARGA HARUS LEBIH DARI 0")
                    elif hp_b > 0 and hp_b < 100000000:
                        data.get("Harga")[cari_n] = hp_b
                        print("\n          === HARGA BERHASIL DIPERBARUI === \n")
                        break
                    else :
                        print("\nHARGA TIDAK BISA LEBIH DARI 100000000")
                except :
                    print("\n PERHATIKAN INPUT")
            break
        elif hm == "t":
            break
        else :
            print("\nPILIHAN TIDAK TERSEDIA ADA")
            
    simpan()
    read()
        

    while True:
        cd = input("\n Apakah anda ingin memperbarui status? (y/t) : ")
        if cd.lower() == "y":
            while True:
                piu = input(" Masukan status baru (OFFLINE/ONLINE) : ").capitalize()
                if piu == "Offline" or piu == "Online":  
                    data["Status"][cari_n] = piu  
                    print("\n         === LAYANAN BERHASIL DIUBAH === \n")
                    break
                else:
                    print("\n STATUS HANYA BOLEH OFFLINE atau ONLINE")
            break
        elif cd.lower() == "t":
            break
        else:
            print("\n PILIHAN TIDAK ADA")
            print(" PERHATIKAN INPUT \n")
    
    simpan()  
    read()    
    print("\n         === DATA BERHASIL DIPERBARUI ===       \n")


#delete
def delete():
    read()
    print("\n         === MENGHAPUS DATA LAYANAN ===        \n")
    while True:
        try:
            hapus_n = str(input("Masukan kode layanan yang akan dihapus : "))
            if hapus_n == "" :
                print("\n INPUT TIDAK BOLEH KOSONG")
            elif hapus_n in data["Kode"]:
                cari_n = data.get("Kode").index(hapus_n)
                data.get("Kode").pop(cari_n)
                data.get("Layanan").pop(cari_n)
                data.get("Harga").pop(cari_n)
                data.get("Status").pop(cari_n)
                print("\n      === DATA LAYANAN BERHASIL DIHAPUS ===\n")
            elif hapus_n not in data["Kode"]:
                print("\n       === KODE TIDAK DITEMUKAN ===\n")

            simpan()
            read()
            break
        except:
            print("\n DATA TIDAK ADA")
            print("SILAHKAN COBA LAGI\n")

#beli layanan
def beli_layanan():
    while True: 
        try:
            print()
            read()  
            simpan()  

            beli = input("Masukkan layanan yang ingin dipilih : ").lower()
            layanan_lower = [layanan.lower() for layanan in data["Layanan"]]

            if beli in layanan_lower:
                cari_layanan = layanan_lower.index(beli)

                if data["Status"][cari_layanan] == "ONLINE":
                    while True:  
                        try:
                            durasi = int(input("Masukkan durasi layanan (1-99) jam : "))
                            if 0 < durasi < 100:
                                cari_kode = data["Kode"][cari_layanan]
                                cari_biaya = data["Harga"][cari_layanan]
                                total_beli = cari_biaya * durasi

                                pembayaran(beli, cari_layanan, durasi, total_beli, cari_kode, cari_biaya, klien, data)
                                break  
                            else:
                                print("\nMASUKKAN DURASI DENGAN BENAR")
                                print("COBA LAGI\n")
                        except ValueError:
                            print("\n PERHATIKAN INPUT, MASUKKAN ANGKA UNTUK DURASI")
                else: 
                    print("\n MOHON MAAF LAYANAN SEDANG OFFLINE/ TERISI")
                    print(" SILAKAN COBA LAYANAN YANG LAIN\n")
            else: 
                print("\n LAYANAN TIDAK ADA")

            
            while True:
                beli_lagi = input("Apakah ingin menyewa layanan lagi? (y/t) : ").lower()
                if beli_lagi == "y":
                    print("\n SILAHKAN PILIH LAYANAN ")
                    break  
                elif beli_lagi == "t":
                    print("\n TERIMA KASIH TELAH MENGGUNAKAN LAYANAN KAMI!")
                    return 
                else:
                    print("\n-> PERHATIKAN INPUT ")
        except Exception as e:
            print(f"\n TERJADI KESALAHAN")

#pembayaran
def pembayaran(beli, cari_layanan, durasi, total_beli, cari_kode, cari_biaya, klien, data):
    while True:
        print("+-----------------------------------------------------+")
        print("|                  METODE PEMBAYARAN                  |")
        print("+-----------------------------------------------------+")
        print("|1. Tunai                                             |")
        print("|2. E-Money                                           |")
        print("+-----------------------------------------------------+")
        print(f" Total pembayaran : Rp {total_beli}")
        pilihan = int(input(" Masukan metode pembayaran = "))
        
        if pilihan == 1:
            uang = int(input("\n  Masukan nominal uang tunai = "))
            if uang >= total_beli:
                kembalian = uang - total_beli
                with open(r"C:\users\lenovo\Desktop\ddp praktikum\struk-pembayaran.txt", "a") as struk:
                    # Menyimpan ke file
                    struk.write("+-------------------STRUK PEMBELIAN--------------------+\n")
                    struk.write(f" Layanan Kesehatan   : {beli}\n")
                    struk.write(f" Kode Layanan        : {cari_kode}\n")
                    struk.write(f" Durasi Layanan      : {durasi} jam\n")
                    struk.write(f" Biaya  Layanan      : Rp {cari_biaya}\n")
                    struk.write("\n")
                    struk.write(f" Total pembayaran    : Rp {total_beli}\n")
                    struk.write(f" Uang                : Rp {uang}\n")
                    struk.write(f" Kembalian           : Rp {kembalian}\n")
                    struk.write("+-----------------------------------------------------+\n")

                # Output ke terminal
                print("+-------------------STRUK PEMBELIAN--------------------+")
                print(f" Layanan Kesehatan   : {beli}")
                print(f" Kode Layanan        : {cari_kode}")
                print(f" Durasi Layanan      : {durasi} jam")
                print(f" Biaya  Layanan      : Rp {cari_biaya}")
                print("")
                print(f" Total pembayaran    : Rp {total_beli}")
                print(f" Uang                : Rp {uang}")
                print(f" Kembalian           : Rp {kembalian}")
                print("+-----------------------------------------------------+\n")
                
                data.get("Status")[cari_layanan] = "Terisi"
                print("\n             === PEMBAYARAN BERHASIL ===               \n")
                break  

            else:
                uang_kurang = total_beli - uang
                print(f" Uang tunai kurang sebesar Rp {uang_kurang}")
                print("\n                 === MOHON MAAF PEMBAYARAN GAGAL ===                \n")

        elif pilihan == 2:
            cari_saldo = klien.get("E-Money")[cari]
            if cari_saldo >= total_beli:
                klien["E-Money"][cari] -= total_beli 
                with open(r"C:\users\lenovo\Desktop\ddp praktikum\struk-pembayaran.txt", "a") as struk:
                    
                    # Menyimpan ke file
                    struk.write("+-------------------STRUK PEMBELIAN--------------------+\n")
                    struk.write(f" Layanan Kesehatan   : {beli}\n")
                    struk.write(f" Kode Layanan        : {cari_kode}\n")
                    struk.write(f" Durasi Layanan      : {durasi} jam\n")
                    struk.write(f" Biaya  Layanan      : Rp {cari_biaya}\n")
                    struk.write("\n")
                    struk.write(f" Total pembayaran    : Rp {total_beli}\n")
                    struk.write(f" Saldo E-Money       : Rp {klien['E-Money'][cari]}\n")
                    struk.write("+-----------------------------------------------------+\n")

                # Output ke terminal
                print("+-------------------STRUK PEMBELIAN--------------------+")
                print(f" Layanan Kesehatan   : {beli}")
                print(f" Kode Layanan        : {cari_kode}")
                print(f" Durasi Layanan      : {durasi} jam")
                print(f" Biaya  Layanan      : Rp {cari_biaya}")
                print("")
                print(f" Total pembayaran    : Rp {total_beli}")
                print(f" Saldo E-Money       : Rp {klien['E-Money'][cari]}")
                print("+-----------------------------------------------------+\n")
                
                data.get("Status")[cari_layanan] = "Terisi"
                print("\n             === PEMBAYARAN BERHASIL ===              \n")
                break  

            else:
                saldo_kurang = total_beli - cari_saldo
                print(f">> Saldo E-Money kurang sebesar Rp {saldo_kurang}")
                print("\n                 === MOHON MAAF PEMBAYARAN GAGAL ===                 \n")
                
                while True:
                    topup = input("Apakah ingin top up E-Money? (y/t) : ")
                    if topup.lower() == "y":
                        os.system("cls")  
                        topup_emoney() 
                        pembayaran(beli, cari_layanan, durasi, total_beli, cari_kode, cari_biaya, klien, data)
                        
                        break
                    elif topup.lower() == "t":
                        print("\n             === SALDO E-MONEY TIDAK CUKUP UNTUK PEMBAYARAN ===           ")    
                        print("                             ---PEMBAYARAN GAGAL---                       \n")
                        break
                    else:
                        print("\n PERHATIKAN INPUT \n")  

        else:
            print("\n PILIHAN TIDAK ADA")
            print("\n COBA LAGI\n")

#topup e-money
def topup_emoney():
    while True :
            print("+-----------------------------------------------------+")
            print("|                   TOP UP E-MONEY                    |")
            print("+-----------------------------------------------------+")
            print("|1. Rp 100.000                                        |")
            print("|2. Rp 200.000                                        |")
            print("|3. Rp 300.000                                        |")
            print("|4. Rp 400.000                                        |")
            print("|5. RP 500.000                                        |")
            print("+-----------------------------------------------------+")
            topup = int(input("\n>> Masukkan pilihan top up e-money : "))
            if topup == 1:
                klien.get("E-Money")[cari] = klien["E-Money"][cari] + 100000
                cari_saldo = klien.get("E-Money")[cari]
                print("\n+-----------------------------------------------------+")
                print(f"Saldo E-Money berhasil ditambah Rp {100000}")
                print(f"Saldo E-Money sekarang Rp {cari_saldo}")
                print("+-----------------------------------------------------+\n")
                print("            === TOP UP E-MONEY BERHASIL ===              \n")
                break

            elif topup == 2:
                klien.get("E-Money")[cari] = klien["E-Money"][cari] + 200000
                cari_saldo = klien.get("E-Money")[cari]
                print("\n+-----------------------------------------------------+")
                print(f"Saldo E-Money berhasil ditambah Rp {200000}")
                print(f"Saldo E-Money sekarang Rp {cari_saldo}")
                print("+-----------------------------------------------------+\n")
                print("            === TOP UP E-MONEY BERHASI L===             \n")
                break

            elif topup == 3:
                klien.get("E-Money")[cari] = klien["E-Money"][cari] + 300000
                cari_saldo = klien.get("E-Money")[cari]
                print("\n+-----------------------------------------------------+")
                print(f"Saldo E-Money berhasil ditambah Rp {300000}")
                print(f"Saldo E-Money sekarang Rp {cari_saldo}")
                print("+-----------------------------------------------------+\n")
                print("            === TOP UP E-MONEY BERHASIL ===             \n")
                break

            elif topup == 4:
                klien.get("E-Money")[cari] = klien["E-Money"][cari] + 400000
                cari_saldo = klien.get("E-Money")[cari]
                print("\n+-----------------------------------------------------+")
                print(f"Saldo E-Money berhasil ditambah Rp {400000}")
                print(f"Saldo E-Money sekarang Rp {cari_saldo}")
                print("+-----------------------------------------------------+\n")
                print("            === TOP UP E-MONEY BERHASIL ===             \n")
                break

            elif topup == 5:
                klien.get("E-Money")[cari] = klien["E-Money"][cari] + 500000
                cari_saldo = klien.get("E-Money")[cari]
                print("\n+-----------------------------------------------------+")
                print(f"Saldo E-Money berhasil ditambah Rp {500000}")
                print(f"Saldo E-Money sekarang Rp {cari_saldo}")
                print("+-----------------------------------------------------+\n")
                print("            === TOP UP E-MONEY BERHASIL ===             \n")
                break

            else:
                print("\nPILIHAN TIDAK ADA")
                print("COBA LAGI\n") 
                break
    with open(pathDataPengguna, "w") as add_klien:
        json.dump(klien, add_klien, indent=4)  
        
#cek saldo e-money
def cek_saldo_emoney():
    cari_saldo = klien.get("E-Money")[cari]
    print("+-----------------------------------------------------+")
    print(f" Saldo E-Money saat ini : Rp {cari_saldo}")
    print("+-----------------------------------------------------+\n")

#menu admin
def menu_admin():
    while True:
        try :
            print("+-----------------------------------------------------+")
            print("|                     MENU ADMIN                      |")
            print("+-----------------------------------------------------+")
            print("|1. Tambah Layanan                                    |")
            print("|2. Lihat Informasi Layanan                           |")
            print("|3. Perbarui Informasi Layanan                        |")
            print("|4. Hapus Layanan                                     |")
            print("|5. Kembali                                           |")
            print("+-----------------------------------------------------+")
            menu = int(input("Masukan menu yang dipilih : "))
            if menu == 1:
                os.system("cls")
                while True:
                    create()
                    Lanjut = input("Apakah anda ingin menambahkan data lagi? (y/t) : ")
                    if Lanjut == "y":
                        print("\nSILAKAN TAMBAH DATA")
                    elif Lanjut == "t":
                        os.system('cls')
                        break
                    else :
                        print("\n PERHATIKAN INPUT")
                break
                    
            elif menu == 2:
                os.system("cls")
                while True :
                    read()
                    Lanjut = input("Apakah anda ingin kembali ke menu admin? (y/t) : ")
                    if Lanjut == "y":
                        os.system('cls')
                        break
                    elif Lanjut == "t":
                        print("\n        === MENAMPILKAN DATA ===   \n")
                    else :
                        print("\n- PERHATIKAN INPUT ")

            elif menu == 3:
                os.system("cls")
                while True:
                    update()
                    Lanjut = input("Apakah anda ingin mengubah data lagi? (y/t) : ")
                    if Lanjut == "y":
                        print("\n SILAKAN UPDATE DATA")
                    elif Lanjut == "t":
                        os.system('cls')
                        break
                    else :
                        print("\n-> PERHATIKAN INPUT")

            elif menu == 4:
                os.system("cls")
                while True:
                    delete()
                    Lanjut = input("Apakah anda ingin menghapus data lagi? (y/t) : ")
                    if Lanjut == "y":
                        print("\n SILAKAN HAPUS DATA ")
                    elif Lanjut == "t":
                        os.system('cls')
                        break
                    else :
                        print("\n PERHATIKAN INPUT")

            elif menu == 5:  
                os.system("cls")
                break

            else:
                print("\n PILIHAN TIDAK ADA")
                print(" COBA LAGI\n")
                menu_admin()
                break

        except ValueError:
            print("\n MASUKAN INPUT DENGAN BENAR")
            print(" COBA LAGI\n")

        except KeyboardInterrupt:
            print("\n PERHATIKAN INPUT")

#menu klien 1
def menu_klien1():
    while True :
        try :
            print("+-----------------------------------------------------+")
            print("|                    MENU KLIEN                       |")
            print("+-----------------------------------------------------+")
            print("|1. Login                                             |")
            print("|2. Registrasi                                        |")
            print("|3. Kembali ke Menu Utama                             |")                  
            print("+-----------------------------------------------------+")
            menu = int(input("Masukkan menu yang dipilih : "))
            if menu == 1:
                os.system("cls")
                login_klien()

            elif menu == 2:
                os.system("cls")
                registrasi_klien()

            elif menu == 3:
                os.system("cls")
                break

            else:
                print("\n PERHATIKAN INPUT ")
                print("COBA LAGI\n")
                break
                
        except ValueError:
            print("\nPERHATIKAN INPUT")
            print(" INPUT HARUS ANGKA\n")  

        except KeyboardInterrupt:
            print("\n-PERHATIKAN INPUT")

#menu klien 2
def menu_klien2():
    try:
        while True:
            print("+-----------------------------------------------------+")
            print("|                    MENU KLIEN                       |")
            print("+-----------------------------------------------------+")
            print("|1. Layanan                                           |")
            print("|2. Top Up E-Money                                    |")
            print("|3. Cek Saldo E-Money                                 |") 
            print("|4. Kembali ke Menu Utama                             |")                 
            print("+-----------------------------------------------------+")
            pilihan = int(input("Masukkan pilihan = "))
            if pilihan == 1:
                os.system("cls")
                beli_layanan()

            elif pilihan == 2:
                os.system("cls")
                topup_emoney()

            elif pilihan == 3:
                os.system("cls")
                cek_saldo_emoney()

            elif pilihan == 4:
                os.system("cls")
                break

            else:
                print("\n- PILIHAN TIDAK ADA")
                print("COBA LAGI")
                break

    except ValueError:
        print("\n BALIK KE MENU AWAL")

    except KeyboardInterrupt:
        print("\n PERHATIKAN INPUT")
    


# main program (fungsi utama untuk menjalankan alur program)
def main_program():
    print("\n             ⋆⁺₊✩🩹🩸₊˚SELAMAT DATANG DI APLIKASI KESEHATANKU ⋆💉⋆⁺₊✧           ")   
    print("                           Tetap Sehat Tanpa Keluar Rumah                           ")
    while True :
        try :
            print()
            print("+-----------------------------------------------------+")
            print("|                      MENU UTAMA                     |")
            print("+-----------------------------------------------------+")
            print("|1. Admin                                             |")
            print("|2. Klien                                             |")
            print("|3. Selesai                                           |")                  
            print("+-----------------------------------------------------+")
            menu = int(input("Masukan menu yang dipilih : "))
            os.system("cls")
            if menu == 1:
                print("============= ANDA MASUK KE MENU ADMIN ============\n")
                login_admin()

            elif menu == 2:
                print("============= ANDA MASUK KE MENU KLIEN=============\n")
                menu_klien1()

            elif menu == 3:
                print("\n============= PROGRAM TELAH SELESAI ===============")
                print("===================TERIMA KASIH ==================\n")
                break

            else:
                print("PILIHAN TIDAK ADA")
                print("COBA LAGI")

        except KeyboardInterrupt:
            print("\n PERHATIKAN INPUT\n")
        except EOFError:
            print("\n PERHATIKAN INPUT\n")
        except ValueError:
            print("\n PERHATIKAN INPUT\n")

main_program()
