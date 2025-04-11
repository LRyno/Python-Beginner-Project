import os

# Header
def header():
    os.system("cls")
    print()
    print(f"{'PROGRAM HITUNG KELILING':^40}")
    print(f"{'DAN LUAS PERSEGI PANJANG':^40}")
    print(f"{'='*40:^40}")

# Input User:
def inputUser():
    calcWhat = str(input("1. Luas\n2. Keliling\nApa yang ingin kamu cari? "))
    panjangPP = int(input("\nBerapa Panjang? "))
    lebarPP = int(input("Berapa Lebar? "))
    return calcWhat,panjangPP,lebarPP

# Calculating 
def calculating(panjangPP,lebarPP):
    luasPP = panjangPP * lebarPP
    kelilingPP = (2 * (panjangPP + lebarPP))
    return luasPP,kelilingPP

# Output
def hasil(calcWhat,luasPP,kelilingPP):
    if calcWhat == "1":
        print(f"\nLuas Persegi Panjang adalah {luasPP}")
    elif calcWhat == "2":
        print(f"\nKeliling Persegi Panjang adalah {kelilingPP}")

while True:
    header()
    calcWhat,panjangPP,lebarPP = inputUser()
    luasPP,kelilingPP = calculating(panjangPP,lebarPP)
    hasil(calcWhat,luasPP,kelilingPP)

    isAgain = str(input("\nUlangi(y/n)? "))
    if isAgain == "n":
        break

print("Akhir dari program, terimakasih.")

# Linggaryno(LRyno)

