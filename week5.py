a = 1
b = 2

sum = a + b
minus = b - a
mull = a * b
div = b / a

#OOP

def sum(a,b,c):
    sum = int(a) + int(b) + int(c)
    return sum

def minus(a,b):
    minus = int(a) - int(b)
    return minus

def mull(a,b):
    mull = int(a) * int(b)
    return mull

def div(a,b):
    div = int(a) / int(b)
    return div


operation = input("1 = sum, 2 = minus, 3 = mull, 4 = div : ")

if operation == "1":
    input1 = input("A = ")
    input2 = input("B = ")
    input3 = input("C = ")
    print("sum = ",sum(input1,input2,input3))
elif operation == "2":
    input1 = input("A = ")
    input2 = input("B = ")
    print("minus = ",minus(input1,input2))
elif operation == "3":
    input1 = input("A = ")
    input2 = input("B = ")
    print("mull = ",mull(input1,input2))
elif operation == "4":
    input1 = input("A = ")
    input2 = input("B = ")
    print("div = ",div(input1,input2))
else:
    print("not found operation")
    

#print("sum = ",sum(10,11,12))
#print("minus = ",minus(10,11))
#print("mull = ",mull(10,11))
#print("div = ",div(10,11))
