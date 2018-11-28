#latihan dictionary

def mainMenu() :
    return input("\nMain Menu : \n 1. Lihat Full Dictionary \n 2. Isi Dictionary \n 3. Searching Dictionary \n 4. Keluar \n\n Pilih : ")

# def lihatFullDictionary(kamusku) 
def menu1(kamusku) :
    print("Full Dictionary : ")
    print("Key:  Value: ")
    for key in kamusku :
        # if(type(kamusku[key]) == type('')) :
        if(str(type(kamusku[key])) == "<class 'str'>") : 
            print("  " + key + " '" + kamusku[key] + "'")
        # elif(type(kamusku[key]) == type(0)) :
        elif(str(type(kamusku[key])) == "<class 'int'>") :
            print("  " + key + "  " + str(kamusku[key]) + "  " + '\n')
      
# def isiDictionary(kamusku) :
def menu2(kamusku) :
    inputJenis = input("Value input 1 untuk string, 2 untuk number? : ")
    inputKey = input("Isi Key : ")
    if(inputJenis == "1") :
        inputValue = input("String Valuenya : ")
        kamusku[inputKey] = inputValue
    elif(inputJenis == "2") :
        inputValue = int(input("Int Valuenya : "))
        kamusku[inputKey] = inputValue
    else :
        print("ngaco!!")

# def searchDictionary(kamusku) :
def menu3(kamusku):
    inputSearch = input("Key search : ")
    kamuskuBaru = {} #buat dictionary kosong baru namanya kamuskuBaru
    for key in kamusku : 
        if(inputSearch.lower() in key.lower()) : 
            kamuskuBaru[key] = kamusku[key]
    menu1(kamuskuBaru)

# def keluar(kamusku)

def menu4(kamusku):
    print("dadah good bye")

#bikin dictionary baru namanya kamuskuBaru
kamuskuBaru = {} 
while True :
    check = mainMenu()
    if(check == "1") :
        menu1(kamuskuBaru)
        # lihatFullDictionary(kamuskuBaru)
    elif(check == "2") :
        menu2(kamuskuBaru)
        # isiDictionary(kamuskuBaru)
    elif(check == "3") :
        menu3(kamuskuBaru)
        # searchDictionary(kamuskuBaru)
    elif(check == "4") :
        menu4(kamuskuBaru)
        #keluar(kamuskuBaru)
        break

#versi lain
# kamuskuBaru = {} 
# listMenu = [menu1,menu2,menu3]
# while True :
#     check = int(mainMenu())
#     if (check == 4) :
#         print("Dadah bhay")
#         break
#     elif(check >= 1 and check <= 3) :
#         listMenu[int(check)-1](kamusku)


