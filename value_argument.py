# 1 whithout return value without argument

def printline():
    print("_"*100)
    return None

printline()

# 2 whithout return value with return argumnet

def printletter(latter,howmanytimes):
    print(latter*howmanytimes)
    return None

printletter('~',100)
print("the easylearn acedamy")
printletter('!',80)

# 3 with return value without argument

def getpi():
    pi=3.141516
    return pi

pi=getpi()
print(f"value of pi={pi}")

# 4 with return value with argument

def toceilcius(fahrenhit):
    ceilcius=(fahrenhit-32) * (5/9)
    return ceilcius

fahrenhit=float(input("enter fehrenhit: "))
ceilcius=toceilcius(fahrenhit)
print(f"ceilcius={ceilcius}")
