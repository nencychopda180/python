def get_dollar(rupees):
    rate=83
    dollars=rupees/rate
    return dollars

rupees=float(input("enter amount in rupees: "))
dollars=get_dollar(rupees)
print(f"{rupees}INR={dollars:.2}USD")