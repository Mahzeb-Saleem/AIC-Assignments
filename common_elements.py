import random
lst_1=[]
for i in range(0,50):
    lst_1.append(random.randint(0,100))
print('1st List of random numbers')
print(lst_1)
lst_2=[]
for j in range(0,50):
    lst_2.append(random.randint(0,100))
print('2nd List of random numbers')
print(lst_2)
common_elements=[]
for i in range(len(lst_1)):
    for j in range(len(lst_2)):
        if lst_1[i]==lst_2[j]:
            common_elements.append(lst_1[i])
print('Common Elements')
print(common_elements)
