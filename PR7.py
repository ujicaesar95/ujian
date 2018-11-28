#mean median modus
#modus kalo semua nilainya sama berarti modus = [] artinya tidak ada modus
numbers = [1,4,2,4,3,2,5,6,3,4,5,6,8,9,7,8,9,7,5,1,2,1,3,4,5,2,1]
# numbers = [1,1,2,2,2,]

def mean1 (numbers):
    numbers.sort()
    return (sum(numbers)/len(numbers)) # jumlah total numbers dibagi panjang list numbers
    
def median1(numbers):
    numbers.sort() # sorting numbers
    mid = len(numbers) // 2 # panjang numbers dibagi 2
    return (numbers[mid] + numbers[~mid]) / 2 # numbers[mid] menghitung list dari kiri ke kanan sampai batas tengah numbers
                                              # numbers[~mid] menghitung list dari kanan ke kiri sampai batas tengah numbers

def Modus1(list) :
    numbers.sort()
    countList = []
    # create countList
    # buat list dalam list [[1,?],[2,?],[3,?], ...  dst]
    for num in list :
        check = False
        for list1 in countList :
            if(list1[0] == num) :
                list1[1] += 1 # buat list1 index ke 1 ditambah 1 
                check = True # check diubah mjd true agar tidak masuk ke if bawahnya
                break
        if(check == False) : # false == false yaitu true
            countList.append([num, 0]) #masukin list kosong countList
    # create list of mode/s
    maxFrequency = 0
    modes = []
    for list1 in countList :
        if (list1[1] > maxFrequency) :
            modes = [list1[0]]
            maxFrequency = list1[1]
        elif (list1[1] == maxFrequency) :
            modes.append(list1[0])
    # if every value appears same amount of times
    if (len(modes) == len(countList)) :
        modes = []
    return modes

print("mean = ", mean1(numbers))
print("median = ",median1(numbers))
print("modus = ", Modus1(numbers))
