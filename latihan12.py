# buat hitung kasir
# misalkan ada uang rupiah pecahan 500, 1000, 5000, 10000, 50000, 100000
# misalkan ada barang yg akan dijual 
# barang 1 = 500
# barang 2 = 1000
# barang 3 = 5000
# uangnya mau disetor ke kasir yang tidak punya uang kembalian diawal
# jadi kasir hanya menerima customer yang punya uang pas untuk barang yg akan dibelinya
# cobain nambahin dictionary ke dalam dictionary yg memiliki key yg sama
uangKasir = {'500' : 0, '1000' : 0, '5000' : 0, '10000' : 0, '50000' : 0, '100000' : 0 }
barang1 = 500
barang2 = 1000
barang3 = 5000
print('barang 1 = ' + str(barang1) + '\n' + 'barang 2 = ' + str(barang2) + '\n' + 'barang 3 = ' + str(barang3) + '\n')
duitCust = int(input('duitCust = '))
n1 = int(input('jumlah barang n1 = '))
n2 = int(input('jumlah barang n2 = '))
n3 = int(input('jumlah barang n3 = '))

def hitungKasir(duitCust, n1, n2, n3) :
    check = 'Yes'
    while duitCust > 0:
        kembalianCust = duitCust - ((barang1*n1)+(barang2*n2)+(barang3*n3))
        if (kembalianCust == 0):
            if (duitCust == 500):
                uangKasir['500'] += 1
            elif (duitCust == 1000):
                uangKasir['1000'] += 1
            elif (duitCust == 5000):
                uangKasir['5000'] += 1
            elif (duitCust == 10000):
                uangKasir['10000'] += 1
            elif (duitCust == 50000):
                uangKasir['50000'] += 1
            elif (duitCust == 100000):
                uangKasir['100000'] += 1

        elif (kembalianCust == 500):
            if (uangKasir['500'] > 0):
                uangKasir['500'] -= 1
            else :
                check = 'No'
                break

        elif (kembalianCust == 1000):
            if (uangKasir['1000'] > 0 and uangKasir['500'] > 1):
                uangKasir['500'] -= 2
            elif(uangKasir['1000'] > 1):
                uangKasir['1000'] -= 1
            else : 
                check = 'No'
                break

        elif (kembalianCust == 5000):
            if(uangKasir['500'] > 9 and uangKasir['1000'] > 4 and uangKasir['5000'] > 0) :
               uangKasir['500'] -= 10 
            elif(uangKasir['1000'] > 4 and uangKasir['5000'] > 0):
                uangKasir['1000'] -= 5
            elif(uangKasir['5000'] > 0):
                uangKasir['5000'] -= 1
            else : 
                check = 'No'
                break

        elif (kembalianCust == 10000):
            if(uangKasir['500'] > 19 and uangKasir['1000'] > 9 and uangKasir['5000'] > 1 and uangKasir['10000'] > 0):
                uangKasir['500'] -= 20
            elif(uangKasir['1000'] > 9 and uangKasir['5000'] > 1 and uangKasir['10000'] > 0) :
                uangKasir['1000'] -= 10
            elif(uangKasir['5000'] > 1 and uangKasir['10000'] > 0):
                uangKasir['5000'] -= 2
            elif(uangKasir['10000'] > 0):
                uangKasir['10000'] -= 1
            else :
                check = 'No'
                break

        elif (kembalianCust == 50000):
            if(uangKasir['500'] > 99 and uangKasir['1000'] > 49 and uangKasir['5000'] > 9 and uangKasir['10000'] > 4 and uangKasir['50000'] > 0):
                uangKasir['500'] -= 100
            elif(uangKasir['1000'] > 49 and uangKasir['5000'] > 9 and uangKasir['10000'] > 4 and uangKasir['50000'] > 0) :
                uangKasir['1000'] -= 50
            elif(uangKasir['5000'] > 9 and uangKasir['10000'] > 4 and uangKasir['50000'] > 0):
                uangKasir['5000'] -= 10
            elif(uangKasir['10000'] > 4 and uangKasir['50000'] > 0):
                uangKasir['10000'] -= 5
            elif(uangKasir['50000'] > 0):
                uangKasir['50000'] -= 1
            else :
                check = 'No'
                break

        elif (kembalianCust == 100000):
            if(uangKasir['500'] > 199 and uangKasir['1000'] > 99 and uangKasir['5000'] > 19 and uangKasir['10000'] > 9 and uangKasir['50000'] > 1 and uangKasir['100000'] > 0):
                uangKasir['500'] -= 200
            elif(uangKasir['1000'] > 99 and uangKasir['5000'] > 19 and uangKasir['10000'] > 9 and uangKasir['50000'] > 1 and uangKasir['100000'] > 0) :
                uangKasir['1000'] -= 100
            elif(uangKasir['5000'] > 19 and uangKasir['10000'] > 9 and uangKasir['50000'] > 1 and uangKasir['100000'] > 0):
                uangKasir['5000'] -= 20
            elif(uangKasir['10000'] > 9 and uangKasir['50000'] > 1 and uangKasir['100000'] > 0):
                uangKasir['10000'] -= 10
            elif(uangKasir['50000'] > 1 and uangKasir['100000'] > 0):
                uangKasir['50000'] -= 2
            elif(uangKasir['100000'] > 0):
                uangKasir['100000'] -= 1
            else :
                check = 'No'
                break
        return check, uangKasir

hasilCheck = hitungKasir(duitCust, n1, n2, n3)
print('Kasir berkata ' + str(hasilCheck))


                


        
                 

