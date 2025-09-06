numbers = [10,20,20,30,40,50]
num = [1,2,3,4,5]
print(numbers)

# add element at the end
numbers.append(60)
print(numbers)

#insert element at specific index
numbers.insert(3,14)
print(numbers)

#remove first occurrence of element
numbers.remove(50)
print(numbers)

#remove element by index (by default last)
numbers.pop()
print(numbers)

#get index of element 
print(numbers.index(30))

#count occurrences of element 
print(numbers.count(20))

#sort list in ascending order
numbers.sort()
print(numbers)

#reverse the list
numbers.reverse()
print(numbers)

#copy list
number2 = numbers.copy()
print(number2)

#add set of values at the end of list
numbers.extend(num)
print(numbers)

#clear all element from list
numbers.clear()
print(numbers)