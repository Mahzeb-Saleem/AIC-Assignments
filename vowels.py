vowels=['a','e','i','o','u']
statement=input('Enter your message: ').lower()
characters=list(statement)
print(characters)
print(vowels)
vowels_found=[]
for i in range (len(characters)):
    for j in range (len(vowels)):
        if characters[i]==vowels[j]:
            vowels_found.append(characters[i])
print(vowels_found)
print(len(vowels_found))

