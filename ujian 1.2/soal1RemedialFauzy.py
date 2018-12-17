arrayUtama = []
arrayGenap = []
arrayGanjil = []

def printMainMenu() :
    inputUser = input("Main Menu : \n 1. User input angka \n 2. Lihat array\n 3. sort array\n 4. Keluar\n\n Pilih Menu : ")
    return inputUser

def inputAngka():
    inputnum = int(input("masukan nilai : "))
    if (inputnum % 2 == 0) :
        arrayUtama.append(inputnum)
        arrayGenap.append(inputnum)
    else:
        arrayUtama.append(inputnum)
        arrayGanjil.append(inputnum)
    

def lihatArray():
    print('lihat array = \n arrayUtama =', str(arrayUtama), '\n arrayGenap =', str(arrayGenap), '\n arrayGanjil =', str(arrayGanjil)  )

def sortArray():
    arrayUtama.sort()
    arrayGenap.sort()
    arrayGanjil.sort()

while True :
    pilihanUser = printMainMenu()
    if(pilihanUser == "1") :
        inputAngka()
    elif(pilihanUser == "2") :
        lihatArray()
    elif(pilihanUser == "3") :
        sortArray()
    elif(pilihanUser == "4") :
        print("Terima Kasih, dan sampai jumpa lagi!!")
        break

