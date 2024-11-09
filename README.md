# PA-KELOMPOK-9

# SISTEM INFORMASI C

# ⋆⁺₊✩🩹🩸₊˚APLIKASI LAYANAN KESEHATAN ONLINE ⋆💉⋆⁺₊✧ 

Nama Anggota Kelompok 9:

1.👩‍💻 Tsabitah Kawiswara     (2409116099)

2.👩‍💻 Jihan Alya Naflah      (2409116082)

3.👩‍💻Vebronia Vitania Lusi  (2409116112)


# ✎✧˚ ༘Library  ⋆｡˚📝
 1. **PrettyTable**     ➺digunakan untuk membuat tabel yang lebih menarik dan teratur. 
 2. **Os berfungsi**    ➺untuk memberikan efek pembersihan layar pada output program. 
 3. **Pwinput**         ➺digunakan untuk menyembunyikan input password yang akan dimasukkan saat program dijalankan. 
 4. **json digunakan**  ➺untuk mengakses modul JSON, yang memungkinkan penguraian data JSON menjadi objek Python.

# Fitur Admin 📱🙎🏻‍♀️
1. Tambah Layanan
2. Lihat Informasi Layanan
3. Perbarui Informasi Layanan
4. Hapus Layanan

# Fitur Pengguna/Klien 📱👥
1. Layanan
2. Top Up E-Money
3. Cek Saldo E-Money


# Penjelasan cara kerja sistem

![github1](https://github.com/user-attachments/assets/022ecce5-3ab9-4cb9-800d-2c34f837bca9)

Pada gambar diatas, adalah pembukaan program yang akan meminta user untuk menginput/memasukkan pilihan menu dengan angka yang sesuai pada tabel yang ditampilkan. Jika memilih 1, maka program akan langsung meminta user untuk mengisi username dan passsword untuk ke menu admin berikutnya. Jika memilih 2, maka program akan menampilkan 2 pilihan menu klien. Jika memilih 3, maka program akan selesai.

![github2](https://github.com/user-attachments/assets/036c0d54-fa29-420b-877e-9707d908a78b)

Gambar diatas adalah tampilan ketika user meimilih 1(Admin), dimana user akan diminta mengisi username dan password sebelum masuk ke menu admin(menjadi admin)


![github3](https://github.com/user-attachments/assets/e33aacab-aef1-48ff-aedc-277733658b6d)

Gambar diatas adalah tampilan ketika user meimilih 2(klien), dimana user akan diminta mengisi username dan password yang sudah terdata atau sudah registrasi, sebelum masuk ke menu klien(menjadi klien)

![github5](https://github.com/user-attachments/assets/9eb5ac79-38f6-4054-98ff-c3d68812f0a9)

Gambar diatas adalah tampilan ketika user memilih 2 (registrasi) pada menu klien, user diminta untukk memasukan username dan password baru yang akan disimpan ke dalam data pengguna, sehingga user dapat login sebagai klien karena sudah memiliki akun (username dan password telah tersimpan).

![github6](https://github.com/user-attachments/assets/bf7d2d4a-c6fe-4531-8ebc-770e2be2a385)

Gambar diatas adalah tampilan menu admin ketika user telah berhasil login menjadi admin, menu yang telah ditampilkan adalah fasilitas admin untuk mengelola data layanan yang dimana layanan tersebut akan dipakai oleh klien. 

![revisi stlh login admin](https://github.com/user-attachments/assets/f1855a81-e0a2-42be-ba41-dbc714b06d3c)

Gambar diatas adalah tampilan ketika admin salah menginput username dan password sehingga gagal untuk login.

![github7](https://github.com/user-attachments/assets/19f10372-dbb6-4bfc-85af-8be8baf89eff)

Gambar diatas adalah tampilan ketika admin memilih nomor 1 (Tambah Layanan), admin akan diminta untuk mengisi kode,layanan, dan harga yang ingin ditambahkan ke dalam tabel layanan, setelah itu program langsung menampilkan tabel data layanan terbaru setelah admin menambahkan data layanan baru.

![revisi jika kode sama](https://github.com/user-attachments/assets/4ef1f098-245a-44ac-b128-62b8a64371cb)

Gambar diatas adalah tampilan ketika admin mengisi kode yang sama untuk melakukan penambahan data, program akan kembali meminta admin untuk mengisi kode yang berbeda agar bisa ditambahkan, berlaku juga pada layanan tidak boleh menambah layanan yang sama.

![github8](https://github.com/user-attachments/assets/438d1b77-9813-4c78-b1fd-630d7f92261c)

Gambar diatas adalah tampilan ketika admin memilih 2(Lihat Informasi Layanan), program akan langsung menampilkan informasi layanan setelah itu program juga akan memberi pilihan kepada admin untuk kembali ke menu admin atau tidak, jika admin memilih tidak maka program kembali menampilkan informasi layanan lagi.

![github9](https://github.com/user-attachments/assets/d649a1e6-a5a2-4e3a-a0db-742219131eef)

Gambar diatas adalah tampilan ketika admin memilih 3 (Perbarui Informasi Layanan). Admin akan diminta untuk memasukan kode, layanan, dan harga yang ingin diperbarui, admin juga dapat merubah data layanan tertentu dengan cara mengisi "t" ketika program menanyakan untuk mengubah data layanan tertentu. Contohnya ketika admin hanya ingin melakukan perubahan pada bagian "Status" maka admin dapat melewati untuk mengubah data layanan dan harga. Setelah admin memasukkan bagian data yang ingin diperbarui, maka program akan menampilkan tabel data layanan terbaru yang menyatakan data berhasil diperbarui.


![github10](https://github.com/user-attachments/assets/4152fbfe-2121-499f-9064-395ec70aa21c)

Gambar diatas adalah tampilan ketika admin memilih 4 (Hapus Layanan). Program akan menampilkan tabel data layanan terlebih dahulu agar admin dapat melihat data layanan mana yang ingin dihapus, setelah itu admin diminta untuk memasukkan kode layanan yang ingin dihapus, setelah itu program akan menampilkan tabel data layanan terbaru yang menyatakan data layanan berhasil dihapus. Setelah itu admin akan ditanya "apakah ingin menghapus data lagi?" jika admin mengisi "t" akan kembali ke menu admin dan jika mengisi "y" akan kembali lagi untuk menghapus data layanan.
![github11](https://github.com/user-attachments/assets/6f14b6ab-8d07-4f7c-a975-a80cdb0f456e)

Gambar diatas adalah tampilan ketika admin memilih 5 (Kembali) pada menu admin. Maka user sekarang kembali ke menu utama (bukan seorang admin lagi), pada menu utama ini, user dapat memilih role sebagai admin atau klien. 

![revisi stlh pilih mnu admin](https://github.com/user-attachments/assets/c0d60d15-3ac0-4b28-a7a5-02747d61c0fd)

Gambar diatas adalah tampilan ketika admin memasukkan pilihan menu berupa huruf sehingga program tidak bisa melanjutkan akses menu.

![github12](https://github.com/user-attachments/assets/72e21f27-6bf3-4dfe-9e6b-27677621ac1b)

Gambar diatas adalah tampilan ketika user memilih 2 (Klien) pada menu utama. Ketika masuk ke menu klien, user menjadi klien dan diminta untuk memasukan menu yang ingin dipilih.

![github13](https://github.com/user-attachments/assets/5b3a1800-9ed7-499d-9e86-a111ea3a76ea)

Gambar diatas adalah tampilan ketika klien memilih 1 (Login). Klien akan diminta untuk memasukkan username dan password yang tentunya sudah terdaftar atau sudah ada dalam data (klien telah melakukan registrasi). Login Klien ini adalah sebagai syarat berlanjutnya program ke menu klien dengan berbagai fitur yaitu layanan, top up e-money, cek saldo e-money, dan kembali ke menu utama.

![github14](https://github.com/user-attachments/assets/73d85a55-3334-4608-8402-22d431ecd135)

Gambar diatas adalah tampilan ketika klien berhasil login. Program akan menampilkan tabel menu klien yang dimana pada menu klien ini lah fasilitas utama bagi klien (pengguna).Lalu klien diminta untuk memasukkan pilihan menu yang akan digunakan.

![github16](https://github.com/user-attachments/assets/594a0a3c-702b-4d17-b4c2-348c5fd04ef6)

Gambar diatas adalah tampilan ketika klien memilih 1 (Layanan) pada menu klien. Program akan menampilkan layanan kesehatan beserta harga/jam dan status dari layanan tersebut, lalu klien diminta untuk memasukkan layanan yang ingin dipilih beserta durasi layanan. Setelah itu program akan menampilkan 2 pilihan untuk metode pembayaran diikuti dengan total pembayaran. Klien akan diminta untuk memilih metode pembayaran, pembayaran akan berhasil jika jumlah saldo (sesuai dengan data saldo masing2 klien) atau uang tunai yang di isi lebih dari total pembayaran dan program akan menampilkan struk pembelian. Jika saldo atau uang tunai kurang dari total pembayaran makan pembayaran gagal

![pembayaran tunai gagal](https://github.com/user-attachments/assets/d0e4d1e2-a22b-4434-9a50-a8c42600294e)

Gambar diatas adalah tampilan ketika saldo e=money klien tidak mencukupi total pembayaran maka pembayaran gagal.


![github17](https://github.com/user-attachments/assets/4457cbe6-124a-44a2-9643-ad7d167a0ef6)

Gambar diatas adalah tampilan ketika klien memilih 2 (Top Up E-Money). Program akan menampilkan pilihan saldo yang ingin di top up, lalu klien diminta untuk memasukkan pilihan jumlah saldo yang ingin di top up. Setelah itu akan ditampilkan jumlah saldo yang bertambah dan update saldo terbaru.

![github18](https://github.com/user-attachments/assets/e912ac94-00a7-42a6-ba59-f6ca1bdd3751)

Gambar diatas adalah tampilan ketika klien memilih 3 (Cek Saldo E-Money). Program akan menampilkan saldo yang dimiliki oleh klien.

![github19](https://github.com/user-attachments/assets/b1d2d6a6-ef77-4188-8425-a4e6b9e9bb4c)

Gambar diatas adalah tampilan ketika klien memilih 4 (Kembali ke Menu Utama) pada amenu klien, lalu user memilih 3 (Selesai) pada menu utama. Program akan selesai dan tidak melanjutkan proses.
