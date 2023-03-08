def hitung_mobil():
    jmS = 0 #jmS artinya jumlah mobil solo
    jmSR = 0 #jmSR artinya jumlah mobil surabaya
    jmJ = 0 #jmJ artinya jumlah mobil jogja
    jmM = 0 #jmM artinya jumlah mobil magelang
    while True:
        asal_mobil = input ("masukkan asal mobil (ketik 'done' untuk keluar) :")
        if asal_mobil == 'done':
            break
        elif asal_mobil == 'solo':
            jmS += 1
        elif asal_mobil == 'surabaya':
            jmSR += 1
        elif asal_mobil == 'jogja':
            jmJ += 1
        elif asal_mobil == 'magelang':
            jmM += 1
        else:
            print("")
    print("Jumlah mobil dari Solo:", jmS)
    print("Jumlah mobil dari Surabaya:", jmSR)
    print("Jumlah mobil dari Jogja:", jmJ)
    print("Jumlah mobil dari Magelang:", jmM)
hitung_mobil()