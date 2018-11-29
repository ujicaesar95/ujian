
def tickets(peopleinline):
    kembalianVas = { "50" : 0, "25" : 0}
    tiket = 25
    check = "YES"

    for duitCust in peopleinline :
        kembalianCust = duitCust - tiket
        if (kembalianCust == 0): # kalo kembalian 0
            kembalianVas['25'] += 1
        elif(kembalianCust == 25) : # kalo kembalian 25
            if(kembalianVas['25'] == 0):
                check = "NO"
                break
            kembalianVas['25'] -= 1 
            kembalianVas['50'] += 1
        elif(kembalianCust == 75): # kalo kembalian 75
            if(kembalianVas['50'] > 0):
                kembalianCust -= 50 
                kembalianVas['50'] -= 1
            if(kembalianVas['25'] < 1):
                check = 'NO'
                break
            kembalianVas['25'] -= kembalianCust / tiket
        return check


print("Vasya berkata = " + str(tickets([25,25,25,50,100])))