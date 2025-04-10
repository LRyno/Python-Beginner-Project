import os

tempSiswa = {
    'nama':'nama',
    'nisn':'10000',
    'semester':1
    }

siswaGroup = {}

while True:
    os.system("cls")
    urutSiswa = 1

    print("\n" + "="*15 + "CATAT DATA SISWA" + "="*15 + "\n")
    NISN = input('Berapa NISN mu? ')
    NAMA = input('Siapa Namamu? ')
    SEM = input('Semester Berapa? ')

    tempSiswa['nisn'] = NISN
    tempSiswa['nama'] = NAMA
    tempSiswa['semester'] = SEM

    siswaGroup[NISN] = {
        'nama':NAMA,
        'semester':SEM
    }
    
    print(f"\n{'NO.':<5} {'NISN':<10} {'NAMA':<10} {'SEMESTER':<5}")
    print("="*40)

    for nisn,data in siswaGroup.items():
        print(f"{urutSiswa:<5} {NISN:<10} {data['nama']:<10} {data['semester']:^9}")
        urutSiswa += 1

    isAgain = str(input('\nLanjut(y/n)? '))

    if isAgain == 'n':
        break
    elif isAgain == 'y':
        continue

print("\nThanks")

#Linggaryno(LRyn)
    