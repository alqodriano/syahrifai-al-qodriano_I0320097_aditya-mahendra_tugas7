#soal1
#alqodriano
print("Laman Penggantian Username")
nama = input("Nama Panggilan Anda : ")
namaamu = nama.upper()
unamemu = input("Username sosial media Anda : ")
username = "@"+unamemu
app = "twiter"
appp = app.capitalize()
print("Hai,", namaamu, "!!",
      "\nSelamat Datang di", appp,
      "\nApakah Anda Yakin akan Mengganti Username Anda" ,username, "? (Y/T)")
keputusan = input(">>")
if keputusan == 'Y' :
    new = input("Masukan Username Baru Anda :")
    print("Selamat Menikmati Fitur Baru Kami dengan Username Baru Anda,",usernamee.replace(unamemu, new), "!!")
else:
    print("Anda Telah Membatalkan Proses Penggantian Username"
          "\nSampai Jumpa !!")