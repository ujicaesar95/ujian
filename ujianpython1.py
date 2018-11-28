#######################################################################################################################
#Nama : Fauzy Caesarrochim
#nomer 1

import math
p = int(input("tahun = "))
p0 = int(input("populasi awal = "))
percent = float(input("percent = "))
percentD = percent/100
aug = int(input("inhabitants = "))
targetp = int(input("target populasi = "))


def  nbYear(p0, percentD, aug, p)  :
    tampung1 = (p0 + (p0 * percentD) + aug)
    x1 = math.floor(tampung1)
    tampung2 = (tampung1 + (tampung1 * percentD) + aug)
    x2 = math.floor(tampung2)
    tampung3 = (tampung2 + (tampung2 * percentD) + aug)
    x3 = math.floor(tampung3)
    if (p == 1 ) :
        print("populasi taun ini = " + str(x1))
        return x1
    elif(p == 2) :
        print("populasi taun ini = " + str(x2))
        return x2
    elif(p == 3) :
        print("populasi taun ini = " + str(x3))
        return x3

hasil = nbYear(p0, percentD, aug, p)

if ( hasil >= targetp):
    print("it will need " +str(p) + " entire years")
else:
    print(" target not satisfied ") 


#######################################################################################################################