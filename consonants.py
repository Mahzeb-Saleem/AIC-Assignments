consonants=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
statement=input('Enter your message: ')
characters=list(statement)
print(characters)
print(consonants)
consonants_found=[]
for i in range (len(characters)):
    for j in range (len(consonants)):
        if characters[i]==consonants[j]:
            consonants_found.append(characters[i])
print(consonants_found)
print(len(consonants_found))
