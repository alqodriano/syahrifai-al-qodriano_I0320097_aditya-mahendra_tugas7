print("Program Latihan Menghitung Diagonal Bidang dan Diagonal Ruang Kubus")
import random
rusuk_kubus = [7, 5.15 , 15.6, 22.222 , 46.43 , 37, 47.8 , 72]
print("Telah disediakan bermacam-macam angka acak sebagai panjang rusuk kubus"
      "\nKetik ONA untuk memulai proses pengacakan angka")
ONA = input(">>")
if ONA == 'ONA' :
    angka_acak = random.choice(rusuk_kubus)
    print("Panjang rusuk kubus :", angka_acak)
    print("Hitunglah Diagonal Ruang dan Diagonal Bidang dengan Panjang Rusuk", angka_acak, "m" )
    print("====================================================================")
    import math
    bidang_kubus = angka_acak * math.sqrt(2)
    print("Diagonal Bidang dari kubus dengan panjang rusuk", angka_acak, "m adalah", bidang_kubus, "m ~", math.ceil(bidang_kubus), "m.")
    ruang_kubus = angka_acak * math.sqrt(3)
    print("Diagonal Ruang dari kubus dengan panjang rusuk", angka_acak, "m adalah", ruang_kubus, "m ~", math.ceil(ruang_kubus), "m.")
else:
    print("Ulang program dan ketik 'ONA' untuk mendapatkan sebuah angka.")