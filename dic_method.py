d1 = {
    'name':'nency',
    'age':21,
    'subject':'python',
}
d2={
    'name':'abc',
    'age':22,
    'subject':'django'
}
print(d1)
d1['ch']=1,2,3
d1['ch_name']=('intro','loop','function')
print(d1)

# clear() removes all items from the dictionary
d2.clear() 
print(d2)

# copy() returns a shallow copy of the dictionary
d2=d1.copy()
print(d2)

# get(key[,d]) return the value of the key .if the key does not exist , returnsd(default yo none)
print(d1.get('ch',0))

# items() returns a new object of the dictionary's item in (key,value)format
print(d1.items())

# keys() returns a new object of the dictionary's keys
print(d1.keys())

# values() the values()method returns a view object that display a list of all the value in the dictionary
print(d1.values())

# fromkeys(seq[,v]) return a new dictionary with keys from seq and value equal to v(default to none)
print(d1.fromkeys('subject',[123,321]))

# pop(key[,d]) removes the item with the key and returnsits value or d if key is not found.if d is not provided and key is not found,it raise keyerror.
print(d2.pop('subject'))
print(d2)

# popitem()removes and return last item(key ,value)raise keyerror if the dictionary is empty
print(d2.popitem)
print(d2)

# update ([other]) update() method adds element(s)to the dictionary from dictionary passed as argument if the key is not in the dictionary then key value will be added.
d2.update({'subject':'cyber security'})
print(d2)

d1.update({'subject':'java'})
print(d1)