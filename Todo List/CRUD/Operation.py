import os
from . import base_data

file_name = "database.txt"

def lihat():
    try:
        with open(file_name,mode="r") as f:
            membaca = f.readlines()
            print("\n"+"="*10+"To-Do List"+"="*10)
            print("-"*30)

            for index,line in enumerate(membaca,start=1):
                print(f"{index}. {line.replace('\n','')}")
    except:
        base_data.no_data_found()

def tambah():
    if not os.path.exists(file_name):
        base_data.no_data_found()
        return

    try:
        with open(file_name,mode="a",encoding="utf-8") as f:
            data_new = (input("\nMasukkan To-Do list: "))
            f.write(data_new + "\n")
            print(f'\nData "{data_new}" ditambahkan.')
    except:
        print("Unknown Error")
   
def hapus():
    if not os.path.exists(file_name):
        base_data.no_data_found()
        return
    
    lihat()
    
    try:
        with open(file_name,mode="r") as f:
            membaca = f.readlines()
        input_user_delete = int(input("\nNomer berapa yang ingin dihapus? "))
        input_user_delete -= 1

        if 0 <= input_user_delete < len(membaca):
            hapus_membaca = membaca.pop(input_user_delete)
            print(f'Menghapus list "{hapus_membaca.strip()}"')

            with open(file_name,mode="w") as f:
                f.writelines(membaca)
    except:
        print("\nUnknown Error")
