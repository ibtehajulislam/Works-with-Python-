vowels = 0
consonants = 0
# Ask the user for an input
statement = input("Enter your word or sentence: ")
for letter in statement:
    if letter.lower() in 'aeiou':
        vowels = vowels + 1
    elif letter == " ":
        pass
    else:
        consonants = consonants + 1

print("There are {} vowels".format(vowels))
print("There are {} consonants".format(consonants))
