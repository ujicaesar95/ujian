#array dimensi
#######################################################################################################################

def mainMenu(theList) : #fungsi main menu kaya hokben
    while True :
        munculkan(theList)
        inputArah = input('diputar ke Kanan atau ke Kiri? : ')
        print("input arah = " + inputArah)
        inputKali = input('diputar berapa kali? : ')
        print("input diputar berapa kali = " + str(inputKali))
        theList = putar(inputArah, int(inputKali), theList)
        inputBerhenti = input('Input 0 untuk keluar dan input yang lain untuk lanjut : ')
        if(inputBerhenti == '0'):
            break
    
def munculkan(theList) : # fungsi munculkan array
    outPut = ''
    for i in range(4) :
        outPut += '\n'
        for j in range(4) :
            outPut += (' ' + str(theList[i][j]))
    print(outPut)


def putar(arah, inputKali, arr) : # fungsi putar
    kali = inputKali % 4 # untuk tidak diputar lebih dari 4x misalnya 5x = 4x + 1x = 1x putar
    newArr = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]] 

    if(kali == 0) : # array tidak berubah
        newArr = arr

    elif((kali == 1 and arah == 'Kanan') or (kali == 3 and arah == 'Kiri')) : # array diputar kekanan 1x atau kekiri 3x
        for i, k in zip(range(4), range(3,-1,-1)) :
            for j in range(4) :
                newArr[j][k] = arr[i][j]

    elif(kali == 2) :
        for i, k in zip(range(4), range(3,-1,-1)) : # array diputar 2x kekanan = 2x kekiri
            for j, l in zip(range(4), range(3,-1,-1)) :
                newArr[k][l] = arr[i][j]

    elif((kali == 3 and arah == 'Kanan') or (kali == 1 and arah == 'Kiri')) : #array diputar kekiri 1x atau kekanan 3x
        for i in range(4) :
            for j, l in zip(range(4), range(3,-1,-1)) :
                newArr[l][i] = arr[i][j]

    arr = newArr
    munculkan(arr)
    return arr

list1 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]];

mainMenu(list1)

testList = [0,1,2,3,4,5]

def test(theList) :
    newList = theList.copy()

    newList[1] = 5
    return newList

test(testList)
print(testList)

#######################################################################################################################

# list1 = [1,2,3,4,5,6,7]
# list2 = []

# for index in range(len(list1)-1, -1, -1) :
#     list2.append(list1[index])

# list2.append(list1[6])
# list2.append(list1[5])
# list2.append(list1[4])
# list2.append(list1[0])

# list1 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
# listHasil = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

# listHasil[0][0] = list1[3][0]
# listHasil[0][1] = list1[2][0]
# listHasil[0][2] = list1[1][0]
# listHasil[0][3] = list1[0][0]

# for i,j in zip(range(4), range(3,-1,-1)) :
#     listHasil[0][i] = list1[j][0]

# listHasil[0][0] = list1[3][0]
# listHasil[0][1] = list1[2][0]
# listHasil[0][2] = list1[1][0]
# listHasil[0][3] = list1[0][0]

# listHasil[1][0] = list1[3][1]
# listHasil[1][1] = list1[2][1]
# listHasil[1][2] = list1[1][1]
# listHasil[1][3] = list1[0][1]

# for i in range(4) :
#     for j,k in zip(range(4), range(3,-1,-1)) :
#         listHasil[i][j] = list1[k][i]


#######################################################################################################################

#score board jam digital seven segment

# from collections import defaultdict

# class Cell:
#     def __init__ (self, width = 4, height = 2, hChar = '*', vChar = '*'):
#         self.width = width
#         self.height = height
#         self.hChar = hChar
#         self.vChar = vChar

#     def showSegments (self, segments):
#         def char (segment):
#             if segment not in segments: return ' '
#             return self.hChar if segment in (0, 3, 6) else self.vChar
#         lines = []
#         lines.append (' ' + char (0) * self.width + ' ')
#         for _ in range (self.height):
#             lines.append (char (1) + ' ' * self.width + char (2) )
#         lines.append (' ' + char (3) * self.width + ' ')
#         for _ in range (self.height):
#             lines.append (char (4) + ' ' * self.width + char (5) )
#         lines.append (' ' + char (6) * self.width + ' ')
#         return lines

# class Display:
#     def __init__ (self, encoding, cells, padding = 1, width = 4, height = 2, hChar = '*', vChar = '*'):
#         self.encoding = encoding
#         self.padding = padding
#         self.cells = [Cell (width, height, hChar, vChar) for _ in range (cells) ]

#     def show (self, string):
#         cellLines = []
#         for idx, c in enumerate (string):
#             if idx >= len (self.cells): break
#             cellLines.append (self.cells [idx].showSegments (self.encoding [c] ) )
#         if not cellLines: return
#         cellLines = zip (*cellLines)
#         print ('\n'.join ( (' ' * self.padding).join (line) for line in cellLines) )

# encoding = defaultdict (lambda: {} )
# encoding ['0'] = {0, 1, 2, 4, 5, 6}
# encoding ['1'] = {2, 5}
# encoding ['2'] = {0, 2, 3, 4, 6}
# encoding ['3'] = {0, 2, 3, 5, 6}

# d = Display (encoding, 5, 2)
# d.show ('12301')

#######################################################################################################################
# 7segmen

# n = input("n = ")

# arr = n.split(' ')
# z = ''

# for i in range(3):
#     if(i == 0):
#         for item in arr:
#             if(item == '2' or item == '3'
#                 or item == '5' or item == '6' or item == '7' or item == '8' or item == '0' or item == '9'):
#                 z += ' _ '
#             else :
#                 z += '   '
#     elif(i == 1):
#         for item in arr:
#             if(item == '8' or item == '9' or item == '4'):
#                 z += '|_|'
#             elif(item == '2' or item == '3'):
#                 z += ' _|'
#             elif(item == '5' or item == '6'):
#                 z += '|_ '
#             elif(item == '1' or item == '7'):
#                 z += '  |'
#             else :
#                 z += '| |'
#     elif(i == 2):
#         for item in arr:
#             if(item == '8' or item == '0' or item == '6'):
#                 z += '|_|'
#             elif(item == '5' or item == '3' or item == '9'):
#                 z += ' _|'
#             elif(item == '2'):
#                 z += '|_ '
#             else :
#                 z += '  |'
#     z += '\n'

# print(z)

#######################################################################################################################


