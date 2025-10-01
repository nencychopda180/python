number=[1,2,3,4,5,6]
evens=filter(lambda x:x%2==0,number)
print(list(evens))
days_in_month = {
    'jan': 31, 
    'feb': 28, 
    'mar': 31,
    'apr': 30, 
    'may': 31
}

res1=filter(lambda x:days_in_month[x]==31,days_in_month)
print(list(res1))
