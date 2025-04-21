import os

class Account:

    def __init__(self,number_account,name_account):
        self.number_account = number_account
        self.name_account = name_account
        self.balance = 0
    
    def cek_saldo(self):
        print(f"Saldo Bank anda: {self.balance}")
    
    def setor_uang(self,amount_setor):
        if amount_setor > 0:
            self.balance += amount_setor
            print(f"anda telah setor {amount_setor}")
        else:
            print("Invalid Error")

    def tarik_uang(self,amount_tarik):
        if 0 < amount_tarik <= self.balance:
            self.balance -= amount_tarik
            print(f"anda menarik saldo {amount_tarik}")
        else:
            print("Saldo di bank anda tidak mencukupi")

    def __str__(self):
        print("\n==========INFORMASI ACCOUNT==========\nNo. Acc: {}\nName Acc: {}".format(
            self.number_account,
            self.name_account
        ))
    
    def menu():
        print("\n==========Selamat datang di aplikasi bank==========\n")
        print("1. Cek Saldo")
        print("2. Setor Tunai")
        print("3. Tarik Tunai")
        print("4. Informasi Account")
        print("5. Keluar")
    
    def main():
        init_Acc  = Account(123456789,"Lingga") 

        while True:
            os.system("cls")
            Account.menu()
            input_init = input("Apa yang ingin anda lakukan? ")
            if input_init == "1":
                init_Acc.cek_saldo()
                isAgain = str(input("\nSelesai(y/n)? "))
                if isAgain == "y" or isAgain == "Y":
                    break

            elif input_init == "2":
                input_amount_setor = int(input("Jumlah Uang disetor: "))
                init_Acc.setor_uang(input_amount_setor)
                isAgain = str(input("\nSelesai(y/n)? "))
                if isAgain == "y" or isAgain == "Y":
                    break

            elif input_init == "3":
                input_amount_tarik = int(input("Jumlah Uang ditarik: "))
                init_Acc.tarik_uang(input_amount_tarik)
                isAgain = str(input("\nSelesai(y/n)? "))
                if isAgain == "y" or isAgain == "Y":
                    break
                
            elif input_init == "4":
                init_Acc.__str__()
                isAgain = str(input("\nSelesai(y/n)? "))
                if isAgain == "y" or isAgain == "Y":
                    break

            elif input_init == "5":
                break

            else:
                print("Invalid Error")

if __name__ == "__main__":
    Account.main()

    


    

