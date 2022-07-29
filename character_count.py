#Type your message for Pakistan on the occasion of 14th August
message=input('Enter your message: ')
print(message)
char=input('Enter the characterof which you want to see repitition: ')
count=0
for i in message.lower():
    if i == char:
        count +=1
        
print('Character'+ repr(char) + 'is repeated' +' ' +repr(count) +' '+ 'times in above message.')
