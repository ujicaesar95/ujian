#######################################################################################################################
#Nama : Fauzy Caesarrochim
#nomer 3

n = int(input("n = "))

def segitiga(n,r=[]):
    for x in range(n):
        l = len(r)
        r = [1 if i == 0 or i == l else r[i-1]+r[i] for i in range(l+1)]
        yield r

def buat(n):
    for p in segitiga(n):
        print(' '.join(map(str,p)).center(n*2)+'\n')

buat(n)