x = input("input number : ")
arr = list(x.split(' '))
z = ""
baris2 = {0: "| |", 1: "  |", 2: " _|", 3: " _|", 4: "|_|", 5: "|_ ", 6: "|_ ", 7: "  |", 8: "|_|", 9: "|_|"}
baris3 = {0: "|_|", 1: "  |", 2: "|_ ", 3: " _|", 4: "  |", 5: " _|", 6: "|_|", 7: "  |", 8: "|_|", 9: " _|"}
for i in range(3):
    for j,k in enumerate(arr):
        if (k == ''):
            break

        intk = int(k)
        if i == 0:
            if (intk == 1 or intk == 4):
                z += "   "
            else:
                z += " _ "
        elif i == 1 :
            z += baris2[intk]
        elif i == 2 :
            z += baris3[intk]
    z += '\n'

print(z)


        

        
    
