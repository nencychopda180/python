marks=int(input("Enter Your Marks:"))

if marks>=33:
    print("result:Pass")

    if marks<=100 and marks>=90:
        print("Grade:A+")
    elif marks<=90 and marks>=75:
        print("Grade:A")
    elif marks<=75 and marks>=60:
        print("Grade:B")
    elif marks<=60 and marks>=45:
        print("Grade:C")
    else:
        print("Grade:D")
else:
    print("result:Fail")