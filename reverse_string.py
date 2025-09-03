text=input("enter a string")
reversed_txt=""
for i in range(len(text)-1,-1,-1):
    reversed_txt+=text[i]
print("reversed string:",reversed_txt)