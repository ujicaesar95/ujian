
#######################################################################################################################

# ****
#  * *
#   **
#    *

n = int(input(" n = "))
for row in range(0,n) :
    for col in range(0,n) :
        if ( (row == 0) or (col == (n-1) ) or (row==col) ) :
            print("*",end="")
        else :
            print(end=" ")
    print()

#######################################################################################################################

# 1
# 2 3
# 4 5 6
# 7 8 9 10

n = int(input(" enter row = "))
num = 1
for row in range(1,n+1):
    for col in range(1,row+1):
        print(num, end=" ")
        num = num +1
    print() 

#######################################################################################################################

# p
# py
# pyt
# pyth
# pytho
# python

string = input(" input the string value = ")
length = len(string)
for row in range(length):
    for col in range(row+1):
        print(string[col],end="")
    print()

#######################################################################################################################

# 1 2 3 4
# 1 2 3
# 1 2
# 1

x = int(input(" value row x = "))
for row in range(x, 0, -1):
    for col in range(1, row+1):
        print(col,end=" ")
    print()

#######################################################################################################################

#    *
#   * *
#  *   *
# * * * *

z = int(input(" value row z = "))
y = 2
for row in range(1, z+1):
    for col in range(1,2*z):
        if ((row+col==z+1) or (col-row==z-1)) :
            print("*",end="")
        elif (row==z and col != y):
                print("*",end="")   
                y = y+2
        else:
            print(end=" ")
    print()

print()

#######################################################################################################################

#  ** **
# *  *  *
# *     *
#  *   *
#   * *
#    *

for row in range(6):
    for col in range(7):
        if ((row==0 and col%3!=0) or (row==1 and col%3==0) or (row-col==2) or (row+col==8)):
            print("*",end="")   
        else:
            print(end=" ")
    print()
print()

#######################################################################################################################
# 1       2       3       4
# 24      14      15      17
# 23      0       0       18
# 22      21      20      19
num =int(input(" enter number of row = "))
n_list = [[0 for x in range (num)]for y in range(num)]
n = 1
low = 0
high = num-1
count = int((num+1)/2)
for i in range(count):
    for j in range(low,high+1):
        n_list[i][j] = n
        n = n+1
    for j in range(low+1,high+1):
        n_list[j][high]=n
        n=n+1
    for j in range(high-1, low-1, -1):
        n_list[high][j]=n
        n=n+1
    for j in range(high-1,low, -1):
        n_list[j][low]=n
        n=n+1

for i in range (num):
    for j in range(num):
        print(n_list[i][j],end='\t')
    print()

#######################################################################################################################

#  *   *
# * * * *
# * * * *
#  * * *
#   * *
#    *

num = int(input(" enter number = "))
n =  num//2
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("* ",end="")
    if num%2==0:
        for j in range(2*(n-i-1)):
            print(" ",end ="")
    else:
        for j in range (2*(n-i-1)+1):
            print(" ",end="")
    for j in range(i+1):
        print("* ",end="")
    print()

for i in range (num,0,-1):
    for j in range(num-i):
        print(" ",end="")
    for j in range(i, 0, -1):
        print("* ",end="")
    print()



#######################################################################################################################

num = int(input(" enter the number = "))
msg = input(" enter the message = ")
l = len(msg)
n = num//2
for i in range(n):
    print(" "*(n-i-1)+"* "*(i+1),end="")
    if num%2==0:
        for j in range(2*(n-i-1)):
            print(" ",end="")
    else:
        for j in range(2*(n-i-1)+1):
            print(" ",end="")
    for j in range(i+1):
        print("* ",end="")
    print()

if num%2==0:
    if l%2==0:
        print("* "*((num-1)//2)+ " ".join(msg) + " *"*((num-1)//2))
    else:
        print("* "*((num-1)//2)+ " ".join(msg) + " *"*(((num-1)//2)+1))
else:
    if l%2==0:
        print("* "*((num-1)//2)+ " ".join(msg) + " *"*(((num-1)//2)+1))
    else:
        print("* "*((num-1)//2)+ " ".join(msg) + " *"*((num-1)//2))

for i in range(num, 0, -1):
    print(" "*(num-i)+ "* "*(i))




#######################################################################################################################

# solve 1
#  *  *  *  *
#  *  *  *
#  *  *
#  *

size = int(input("Masukkan size: "))
z = ""

for num in range(size):
    for num1 in range(num, size):
        z += " * "
    z += "\n"

print(z)
#######################################################################################################################
# solve 2
#  *  *  *  *
#  *  *  *
#  *  *
#  *
#  *  *
#  *  *  *
#  *  *  *  *
size = int(input("Masukkan size: "))
z = ""

for num in range(size):
    for num1 in range(num, size):
        z += " * "
    z += "\n"
for num in range(size-1):
    for num1 in range(num+2):
        z += " * "
    z += "\n"

print(z)
#######################################################################################################################
# solve 3
#           *
#        *  *  *
#     *  *  *  *  *
#  *  *  *  *  *  *  *
size = int(input("Masukkan size: "))
z = ""

for num in range(size):
    for num1 in range(size-1-num):
        z += "   "
    for num2 in range((num*2)+1):
        z += " * "
    z += "\n"

print(z)
#######################################################################################################################
# solve 4
#  *  *  *  *  *  *  *
#     *  *  *  *  *
#        *  *  *
#           *
size = int(input("Masukkan size: "))
z = ""

for num in range(size):
    for num1 in range(num):
        z += "   "
    for num2 in range((size*2)-(num*2)-1):
        z += " * "
    z += "\n"

print(z)
#######################################################################################################################
# solve 5
#           *
#        *  *  *
#     *  *  *  *  *
#  *  *  *  *  *  *  *
#     *  *  *  *  *
#        *  *  *
#           *
size = int(input("Masukkan size: "))
z = ""

for num in range(size):
    for num1 in range(size-1-num):
        z += "   "
    for num2 in range((num*2)+1):
        z += " * "
    z += "\n"
for num in range(1, size):
    for num1 in range(num):
        z += "   "
    for num2 in range((size*2)-(num*2)-1):
        z += " * "
    z += "\n"

print(z)
#######################################################################################################################
# solve 6
#  *  *  *  *  *  *  *
#  *  *  *     *  *  *
#  *  *           *  *
#  *                 *
#  *  *           *  *
#  *  *  *     *  *  *
#  *  *  *  *  *  *  *
size = int(input("Masukkan size: "))
z = ""

for num in range(size):
    for num1 in range(num, size):
        z += " * "
    for num2 in range(0, (num*2)-1):
        z += "   "
    for num3 in range(size, num, -1):
        if(num3 == 1):
            break
        z += " * "
    z += "\n"
for num in range(size-1):
    for num1 in range(0, num+2):
        z += " * "
    for num2 in range(size*2-5, num*2, -1):
        z += "   "
    for num3 in range(0, num+2):
        if(num == size-2 and num3 == num+1):
            break
        z += " * "
    z += "\n"

print(z)
#######################################################################################################################   