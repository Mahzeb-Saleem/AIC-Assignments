word=input('Enter a single word: ')
character=list(word)
print(character)
print(len(character))
print(character[::-1])

# character[::-1] is a fuction which returns the reverse of character
# For even no of characters, if character equals its reverse then its a palindrome

if character == character[::-1]:
    print("Yes, it's a palindrome")
else:
    print("No, it's not a palindrome")
