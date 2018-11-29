
p0 = int(input("p0 = "))
percent = int(input("percent = "))
aug = int(input("aug = "))
p = int(input("p target = "))


def nbyear(p0, percent, aug, p):
    year = 0
    while p0<p : #while true
        p0 = p0 + (p0 * percent/100) + aug #p0 nya ditimpa 
        year += 1 #kalo udah selesai ditambahin 1
    return year #balikin nilai year



print("target populasi selama " + str(nbyear(p0, percent, aug, p) + ' tahun' ))
# print(nbyear(1000,2,50,1200))
