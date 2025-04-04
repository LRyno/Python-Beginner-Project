print(26*"=")
print("Latihan Membentuk Gambar")
print(26*"=")
print("\n")

inUser = int(input("""Apa yang ingin anda gambar
1. Menara
2. Segitiga
3. Persegi Panjang
Pilih dengan angka: """))

if inUser == 1:
    dataTinggiReq = int(input("Tinggi berapa? "))
    dataBaris = 0
    while True:
        print(" " * 5 + "=" * dataTinggiReq)
        dataBaris += 1
        if dataTinggiReq == dataBaris:
            break
        elif dataTinggiReq != dataBaris:
            continue

elif inUser == 2:
    dataReq = int(input("Berapa sisi? "))
    dataSisi = 0
    dataSpasi = dataReq

    while True:
        dataSisi += 1
        if dataReq == dataSisi:
            print("Cukup")
            break
        elif dataSisi % 2:
            print(" " * dataSpasi + "*" * dataSisi)
            dataSpasi -= 1  
        else:
            continue

elif inUser == 3:
    dataReqPanjang = int(input("Berapa Panjang? "))
    dataPanjang = 0
    dataTinggiMax = dataReqPanjang // 4
    dataTinggi = 0

    while True:
        dataTinggi += 1
        print(" " * 5 + dataReqPanjang * "+")
        if dataReqPanjang != dataReqPanjang:
            continue
        elif dataTinggiMax == dataTinggi:
            break

else:
    print("Error Occured")