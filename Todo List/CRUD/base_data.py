def no_data_found():
    with open("database.txt",mode="w",encoding="utf-8") as f:
            print("Todo List tidak ada. Membuat baru")
            f.write(f'')