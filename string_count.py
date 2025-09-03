text=(input("enter a string"))
digits=0
letter=0
vowels=0
consonants=0
symbol=0
for string in text:
    if string.isdigit():
        digits+=1
    elif string.isalpha():
        letter+=1
       
        if string.lower() in "aeiou":
                vowels+=1
        else :
             consonants+=1
    else:
        symbol+=1
       
print("Digits:",digits)
print("letter:",letter)
print("vowels:",vowels)
print("consonants:",consonants)
print("symbol:",symbol)
    