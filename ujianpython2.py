
#######################################################################################################################
#nomer 2

purchamt=float(input("Enter the cost of the item purchased: "))
payamt=float(input("Enter the amount paid for the item: "))

def main():
calcchange(purchamt, payamt)
printresults (change)
return

def calcchange(purchamt, payamt):
change = payamt - purchamt
print("change = "change)
return change

def printresults(change):
print ("Amount of change to give back: ", change)
return

main()

#######################################################################################################################