import os
import CRUD

if __name__ == "__main__":
    while True:
        if os.name == "posix":
            os.system("clear")
        elif os.name == "nt":
            os.system("cls")
    
        print("="*10 + "TO-DO LIST" + "="*10)
        print("1. Lihat Daftar Tugas✅")
        print("2. Tambah Tugas➕")
        print("3. Hapus Tugas❌")
        print("0. Quit")
    
        user_option = str(input("\nMasukkan Opsi: "))
        match user_option:
            case "1":
                CRUD.lihat()
            case "2":
                CRUD.tambah()
            case "3":
                CRUD.hapus()
            case "0":
                break

        isAgain = str(input("\nSelesai(y/n)? "))
        if isAgain == "y" or isAgain == "Y":
            break
    
        