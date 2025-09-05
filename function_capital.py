def get_capital(country):
   capital={
     
    "India":"New Delhi",
    "USA":"Washington,D.C",
    "UK":"London",
    "France":"Paris",
    "Germany":"Berlin",
    "Japan":"Tokyo",
    "China":"Beijing",
    "Canada":"Ottawa",
    "Austraila":"Canberra",
    "Brazil":"Brasilla",
    
    }
   return capital.get(country,"capital not found")

country=input("enter country name: ")
print(f"capital of {country} is {get_capital(country)}")
