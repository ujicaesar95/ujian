#######################################################################################################################

#  ***
# *   *
# *   *
# *****
# *   *
# *   *
# *   *

str1 =""
for row in range(7) :
    for col in range(5):
        if (((col == 0 or col == 4) and row!=0) or ((row == 0 or row == 3) and (col>0 and col<4))):
        # if ((col == 0 or col == 4)  or ((row == 0 or row == 3) and (col>0 and col<4)):
            str1 = str1 + "*"
        else :
            str1 = str1 + " "
    str1 = str1+"\n"
"\n"
print(str1)

#######################################################################################################################

# ****
# *   *
# *   *
# ****
# *   *
# *   *
# ****

for row in range(7):
    for col in range(5):
        if ((col == 0) or (col == 4 and (row != 0 and row != 3 and row != 6)) or ((row == 0 or row == 3 or row == 6) and (col>0 and col<4))):
            # ((col == 0) or (col == 4 ) or ((row == 0 or row == 3 or row == 6) and (col>0 and col<4))):
            print("*",end="")
        else :
            print(end=" ")
    print()
"\n"

#######################################################################################################################

#  ****
# *
# *
# *
# *
# *
#  ****

for row in range(7):
    for col in range(5):
        if ((col == 0 and (row != 0 and row != 6)) or ((row == 0 or row == 6)) and (col > 0)) :
            # ((col == 0 ) or ((row == 0 or row == 6)) and (col > 0)) :
            print("*",end="")
        else :
            print(end=" ")
    print()
"\n"

#######################################################################################################################

# ****
# *   *
# *   *
# *   *
# *   *
# *   *
# ****
for row in range(7):
    for col in range(5):
        if(col == 0) or (col == 4 and (row != 0 and row != 6)) or (row == 0 or row == 6 ) and (col > 0 and col < 4):
            print("*",end="")
        else :
            print(end=" ")
    print()
"\n"

#######################################################################################################################

# *****
# *
# *
# *****
# *
# *
# *****

for row in range(7):
    for col in range(5):
        if((col == 0) or (row == 0 or row == 3 or row ==6) and (col>0) ):
            print("*",end="")
        else :
            print(end=" ")
    print()
"\n"

#######################################################################################################################

# *****
# *
# *
# *****
# *
# *
# *

for row in range(7):
    for col in range(5):
        if((col == 0) or (row == 0 or row == 3 ) and (col>0) ):
            print("*",end="")
        else :
            print(end=" ")
    print()
"\n"

#######################################################################################################################

# *****
# *
# *
# *  **
# *   *
# *   *
# *****

for row in range(7):
    for col in range(5):
        if((col == 0) or (col == 4 and (row != 1 and row != 2)) or ((row == 0 or row == 6) and (col > 0 and col<4) ) or (row == 3  and (col == 3  ) )):
            print("*",end="")
        else :
            print(end=" ")
    print()
"\n"

#######################################################################################################################

# *   *
# *   *
# *   *
# *****
# *   *
# *   *
# *   *

for row in range(7):
    for col in range(5):
        if((col == 0) or (col == 4) or (row == 3 and (col >0 and col < 4))):
            print("*",end="")
        else :
            print(end=" ")
    print()
"\n"

#######################################################################################################################

# *****
#   *
#   *
#   *
#   *
#   *
# *****

for row in range(7):
    for col in range(5):
        if((col == 2) or ((row == 0 or row == 6) and col != 2 )):
            print("*",end="")
        else :
            print(end=" ")
    print()
"\n"

#######################################################################################################################

# *****
#   *
#   *
#   *
#   *
#   *
# ***

for row in range(7):
    for col in range(5):
        if((col == 2) or (row == 0  and col != 2 ) or (row ==6 and col < 2)):
            print("*",end="")
        else :
            print(end=" ")
    print()
"\n"

#######################################################################################################################

# *   *
# *  *
# * *
# **
# * *
# *  *
# *   *

i = 0
j = 4
for row in range(7):
    for col in range(5):
        if((col == 0) or (row == col+2 and col > 1) and col > 0):
            print("*",end="")
        elif (row == i and col == j):
            print("*",end="")
            i = i+1
            j = j-1

        else :
            print(end=" ")
    print()
"\n"

#######################################################################################################################

# *
# *
# *
# *
# *
# *
# *****

for row in range(7):
    for col in range(5):
        if ((col == 0 ) or ((row > 0 and row == 6)) ) :  
            print("*",end="")
        else :
            print(end=" ")
    print()
"\n"

#######################################################################################################################

# *     *
# **   **
# * * * *
# *  *  *
# *     *
# *     *
# *     *

for row in range(7):
    for col in range(7):
        if ((col == 0 or col == 6) or ((row == col )and (col > 0 and col <4)) or (row == 1 and col ==5) or (row == 2 and col == 4) ) :  
            print("*",end="")
        else :
            print(end=" ")
    print()
"\n"

#######################################################################################################################

# *     *
# *     *
# **    *
# * *   *
# *  *  *
# *   * *
# *    **
# *     *

for row in range(7) :#6
    for col in range(7):#6
        if ((col == 0 or col == 6) or (row == col ) ) :
        # if ((col == 0 or col == 5) or (row == col and (col > 0 and col < 5) ) ) :  
            print("*",end="")
        else :
            print(end=" ")
    print()
"\n"

#######################################################################################################################

#  ***
# *   *
# *   *
# *   *
# *   *
# *   *
#  ***

for row in range(7):
    for col in range(5):
        if(((col == 0 or col == 4) and (row != 0 and row != 6)) or ((row == 0 or row == 6) and (col > 0 and col < 4))):
            print("*",end="")
        else :
            print(end=" ")
    print()
"\n"

#######################################################################################################################

# ****
# *   *
# *   *
# ****
# *
# *
# *

for row in range(7):
    for col in range(5):
        if((col == 0) or (col == 4 and (row == 1 or row == 2)) or ((row == 0 or row == 3 ) and (col > 0 and col < 4))):
            print("*",end="")
        else :
            print(end=" ")
    print()
"\n"

#######################################################################################################################

#  ***
# *   *
# *   *
# *   *
# *   *
# **  *
#  ***
#     *

for row in range(8):
    for col in range(5):
        if( ((col == 0 or col == 4) and (row > 0 and row < 6)) or ((row == 0 or row == 6) and (col > 0 and col < 4)) or ((row == 5 and col ==1) or (row == 7 and col == 4)) ):
            print("*",end="")
        else :
            print(end=" ")
    print()
"\n"

#######################################################################################################################

# ****
# *   *
# *   *
# ****
# *   *
# *   *
# *   *

for row in range(7):
    for col in range(5):
        if ( (col == 0) or (col ==4 and (row !=0 and row != 3)) or ((row == 0 or row ==3) and(col > 0 and col < 4)) ) :
            print("*",end="")
        else :
            print(end=" ")
    print()
"\n"

#######################################################################################################################

#  ***
# *
# *
#  ***
#     *
#     *
#  ***

for row in range(7):
    for col in range(5):
        if ( (( row == 0 or row == 3 or row == 6) and (col > 0 and col < 4)) or (col == 0 and (row > 0 and row < 3)) or (col == 4 and (row > 3 and row < 6)) ) :
            print("*",end="")
        else :
            print(end=" ")
    print()
"\n"

#######################################################################################################################

# *****
#   *
#   *
#   *
#   *
#   *
#   *

for row in range(7):
    for col in range(5):
        if((row == 0 and (col > 0 or col < 6)) or ( col == 2 and ( row > 0))):
            # ((col ==2) or (row == 0 and col != 2))
            print("*",end="")
        else :
            print(end=" ")
    print()
"\n"


#######################################################################################################################

# *   *
# *   *
# *   *
# *   *
# *   *
# *   *
#  ***

for row in range(7):
    for col in range(5):
        if( ((col == 0 or col == 4 ) and row != 6) or (row == 6 and (col > 0 and col < 4)) ):
            print("*",end="")
        else :
            print(end=" ")
    print()
"\n"

#######################################################################################################################

# *     *
#  *   *
#   * *
#    *

i = 0
j = 6

for row in range(4):
    for col in range(7):
        if(row==col ):
            print("*",end="")
        elif (row == i and col == j):
            print("*",end="")
            i = i+1
            j = j-1
        else :
            print(end=" ")
    print()
"\n"

#######################################################################################################################

# *  *  *
# * * * *
# **   **
# *     *

i = 0
j = 3
for row in range(4):
    for col in range(7):
        if( (col == 0) or (col == 6) or (col == 5 and row == 2) or (col == 4 and row == 1) ):
            print("*",end="")
        elif (row == i and col == j):
            print("*",end="")
            i = i+1
            j = j-1
        else :
            print(end=" ")
    print()
"\n"

#######################################################################################################################

# *   *
#  * *
#   *
#  * *
# *   *

i = 0
j = 4
for row in range(5):
    for col in range(5):
        if (row == i and col == j):
            print("*",end="")
            i = i+1
            j = j-1
        elif( col == row ):
            print("*",end="")
        else :
            print(end=" ")
    print()
"\n"

#######################################################################################################################

# *   *
#  * *
#   *
#   *
#   *

for row in range(5):
    for col in range(5):
        if( (col == 2 and row > 1) or (row == col and col < 2) or (row == 1 and col == 3 ) or (row == 0 and col == 4 ) ):
            print("*",end="")
        else :
            print(end=" ")
    print()
"\n"

#######################################################################################################################

# ******
#     *
#    *
#   *
#  *
# ******

i = 1
j = 4

for row in range(0,6,1):
    for col in range(0,6,1):
        if (row == 0 or row == 5):
            print("*",end="")
        elif (row == i and col == j):
            print("*",end="")
            i = i+1
            j = j-1
        else :
            print(end=" ")
    print()
"\n"

#versi lain Z
# i = 0
# j = 4

# for row in range(5):
#     for col in range(5):
#         if (row == i and col == j):
#             print("*",end="")
#             i = i+1
#             j = j-1
#         elif ( (row == 0 and (col > 0 and col < 5)) or (row == 4 and (col > 0 and col , 5)) ) :
#             print("*",end="")
#         else :
#             print(end=" ")
#     print()
# "\n"


            
