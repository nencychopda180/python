age=int(input("enter your age: "))
balance=50000
if age < 18:
    print("you are under 18 payment not allow")
else:
    balance=int(input("enter your balance"))

    amount=int(input("enter amount to pay"))

    if amount<=balance:
     balance-=amount
     print(f"payment successful")
     print(f"remaining balance:{balance}")

    else:
     print("payment failed")

