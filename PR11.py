x = float(input("x = "))
y = float(input("y = "))
operator = input("masukan operator \n 1. 'add' untuk + \n 2. 'sub' untuk - \n 3. 'div' untuk / \n 4. 'mul' untuk * \n your input : ")

def fungsi(operator, x, y):
    if operator == "add" :
        return x + y
    elif operator == "sub" :
        return x - y
    elif operator == "div" :
        return x / y
    elif operator == "mul" :
        return x*y
    else:
        return operator


def dictio(operator, x, y):
    return{
        'add' : lambda: x+y,
        'sub' : lambda: x-y,
        'mul' : lambda: x*y,
        'div' : lambda: x/y,
    }.get(operator, lambda: None)()

value = fungsi(operator, x, y)

print("Value = "+ str(value))

#####################################################################

userid = int(input(" key userid : "))

name_id = {
    '1' : "aku",
    '2' : "kamu",
    '3' : "dia",
    '4' : "anda",
}

def greeting1(userid):
    if userid in name_id :
        return "Hi %s" % name_id[userid]
    else :
        return "Haloo"


def greeting2(userid):  
    return "Hi %s ! " % name_id.get(userid, "there")

vargreet = greeting1(userid)

print("greeting1 = " + str(vargreet))
print("greeting2 = " + greeting2(userid))

#####################################################################

dict_vec = {
    'x' : 1,
    'y' : 2,
    'z' : 3,
}

def func_print_vec(x, y, z):
    print('<%s, %s, %s>' % (x,y,z))

func_print_vec(**dict_vec)