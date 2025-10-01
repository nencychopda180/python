import random

print(random.random())

print(random.uniform(10,70))

print(random.randint(10,90))

print(random.randrange(10,90,10))

lit=[10,20,30,40,50,60]

print(random.choice(lit))

print(random.choices(lit,k=3))

print(random.shuffle(lit))
print(lit)

print(random.sample(lit,2))