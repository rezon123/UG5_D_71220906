def ganti_kata(k, c, g): #k artinya kalimat, c artinya cari, g artinya ganti, kb artinya kalimat baru
    k = k.split()   
    for i in range(len(k)):
        if k[i] == c:
            k[i] = g
    kb = " ".join(k)
    return kb
k = input("Masukkan kalimat: ")
c = input("kata yang ingin dicari: ")
g = input("diganti menjadi: ")
kb = ganti_kata(k, c, g)
print("Kalimat baru:", kb)