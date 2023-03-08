import math
while True:
    inputan = input("Masukkan jarak awal Rendy dengan helikopter (dalam meter): ")
    inputan1= input("masukkan sudut elevasi pada menit ke-5 (dalam meter): ")
    inputan2= input("masukkan sudut elebasi pada menit ke-6 (dalam meter): ")
    jarak_awal = sudut5, sudut6 = map(float, inputan.split())
    tinggi_awal = jarak_awal * math.tan(math.radians(sudut5))
    jarak_akhir = jarak_awal * (math.tan(math.radians(sudut6)) - math.tan(math.radians(sudut5)))
    selisih_ketinggian = jarak_akhir * math.tan(math.radians(sudut6))
    jarak_vertikal = selisih_ketinggian - tinggi_awal
    print("Jarak vertikal helikopter adalah ")