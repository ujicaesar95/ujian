#         1
#     3       5
# 7       9       11
# [[1],[3,5],[7,9,11]]
def rowSumOddNumbers(n):
    theList = []
    nilai = 1

    for i in range(1, n+1):
        rowList = []
        for j in range(i):
            rowList.append(nilai)
            nilai += 2
        theList.append(rowList)
    return theList

row = int(input("row = "))
listHasil = rowSumOddNumbers(row)
print(listHasil)
print(sum(listHasil[row-1]))

z = ''
for listRow, i in zip(listHasil, range(len(listHasil))):
    for j in range(row-i):
        z += '  '
    for num in listRow :
        z += str(num)
        for k in range(4 - len(str(num))):
            z += ' '
    z += '\n'

print(z)