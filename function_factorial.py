def get_factorial(n):
    result=1
    for i in range(1,n+1):
        result*=i
    return result

num=int(input("enter a number: "))
print(f"factorial of {num} = {get_factorial(num)}")