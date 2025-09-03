line=input("enter one line ")
vowels=0
for letter in line:
    if letter=='a' or letter=='e' or letter=='i' or letter=='o' or letter=='u':
        vowels=vowels+1
print(vowels)