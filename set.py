s1={'apple','banana','kiwi','orange','apple','kiwi'}
s2={'apple','mango','cherry'}
print(s1)
print(s2)
s1.add('mango')
print(s1)
s1.remove('apple')
print(s1)

union=s1.union(s2)
print(union)
union=s2.union(s1)
print(union)

intersection=s1.intersection(s2)
print(intersection)
intersection=s2.intersection(s1)
print(intersection)

difference=s1.difference(s2)
print(difference)
difference=s2.difference(s1)
print(difference)