print(26*"=")
print("Latihan Kalkulator 2 Digit")
print(26*"=")
print("\n")

userInput = input("(+ - * /): ")
inputAngka = float(input("Angka 1: "))
inputAngka2 = float(input("Angka 2: "))

if userInput == "+":
    hasilOperasi = inputAngka + inputAngka2
    print(f"Hasil = {hasilOperasi}")
elif userInput == "-":
    hasilOperasi = inputAngka - inputAngka2
    print(f"Hasil = {hasilOperasi}")
elif userInput == "*":
    hasilOperasi = inputAngka * inputAngka2
    print(f"Hasil = {hasilOperasi}")
elif userInput == "/":
    hasilOperasi = inputAngka / inputAngka2
    print(f"Hasil = {hasilOperasi}")
else:
    print("Error")