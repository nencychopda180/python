num =int(input("enter numbe"))
for multiplier in range(1,11):
    result=num*multiplier
    print(f"{num} X {multiplier:2} = {result:3}")
    multiplier=multiplier+1
    