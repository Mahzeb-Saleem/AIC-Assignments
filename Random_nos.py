import random
random_nos=[]
mod_nos=[]
sum=0
for i in range(0,100):
    random_nos.append(random.randint(0,200))
print('List of random numbers')
print(random_nos)
min=random_nos[0]
max=random_nos[0]

for j in range(0,99):
    if random_nos[j]>40:
        mod_nos.append(random_nos[j])
print('List of random numbers greaater than 40')
print(mod_nos) 

for k in range(len(random_nos)):
    sum=random_nos[k]+sum
print('Sum of random numbers')
print(sum)

for l in range(len(random_nos)):
    if random_nos[l]<min:
        min=random_nos[l]
print('Minimum of random numbers')
print(min)

for m in range(len(random_nos)):
    if random_nos[m]>max:
        max=random_nos[m]
print('Maximum of random numbers')
print(max)

average_rand=sum/()



