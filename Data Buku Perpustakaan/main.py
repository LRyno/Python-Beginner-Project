listBook = []

while True:
    print("="*15 + " Data Buku Perpustakaan " + "="*15)
    titleBook = (input("\nMasukkan Judul: "))
    authorBook = (input("Masukkan Penulis: "))
    yearOfBook = int(input("Terbit Pada: "))

    newBook = [titleBook,authorBook,yearOfBook]
    listBook.append(newBook)

    print("\nNo\t Judul\t\t Penulis\t Terbit")
    print("-"*50)
    for no,book in enumerate(listBook):
        print(f"{no+1}\t {book[0]}\t\t {book[1]}\t\t {book[2]}")

    userAgain = str(input("\nInput Lagi? (y/n): "))
    if userAgain == "n":
        break

