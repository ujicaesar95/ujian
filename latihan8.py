# oy =[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

# out = ''

# # for i in range(len(oy)):
# #     for j in oy[i]:
# #         out += str(j) + ' '
# #     out += '\n'

# for i in range(len(oy)):
#     for j in range(len(oy[i])):
#         out += str(oy[i][j]) + ' '
#     out += '\n'

# print(out)

#n = 8784204
#t = 4-0+2-4+8-7+8 = 11
#11%11=0

# n = int(input("input n ="))
# tampunglist = []
# strtamplist = str(tampunglist)
# print(strtamplist(n))

# def num (numbers):
#     int(input("n ="))
#     n = len(numbers)
#     return (numbers[~n])

# print("n = ", num(numbers))
    
import math

n = int(input('n = '))
t = 0
op = True

while(n>0):
    if(op):
        t += n % 10
    else:
        t -= n % 10
    
    op = not(op)
    n = math.floor(n/10)

print(t)
if(t%11==0):
    print("yes")
else:
    print("no")



