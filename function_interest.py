def get_interest(amount,rate,year):
    interest=(amount*rate*year)/100
    return interest

amount=float(input("enter amount: "))
rate=float(input("enter rate: "))
year=float(input("enter year: "))

interest=get_interest(amount,rate,year)
print(f"simple interest={interest}")