import collections
arrayUtama = []

def printMainMenu() :
    inputUser = input("Main Menu : \n 1. User input angka \n 2. Lihat array\n 3. search array\n 4. Keluar\n\n Pilih Menu : ")
    return inputUser

def inputAngka():
    inputnum = int(input("masukan nilai : "))
    arrayUtama.append(inputnum)

def lihatArray():
    print('lihat array = \n arrayUtama = ', str(arrayUtama) )

def searchArray():
    angkaSearch = int(input('Angka yang dicari = '))
    jumlahSeacrh = collections.Counter(arrayUtama)
    indexSearch = [i for i,x in enumerate(arrayUtama) if x==angkaSearch] 
    print( 'Jumlah angka yang dicari = ', str(jumlahSeacrh), '\n Index angka yang dicari = ', str(indexSearch) )

while True :
    pilihanUser = printMainMenu()
    if(pilihanUser == "1") :
        inputAngka()
    elif(pilihanUser == "2") :
        lihatArray()
    elif(pilihanUser == "3") :
        searchArray()
    elif(pilihanUser == "4") :
        print("Terima Kasih, dan sampai jumpa lagi!!")
        break
