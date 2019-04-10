# Ask user for name:

name = input('What is your name?: ')


# ask user for their age:

age = input('What is your age?: ')


#Ask user for city:

city = input('What is your city?: ')


# Ask user what they enjoy:

enjoy = input('What do you love doing?: ' )

#Create output test:

string = 'Hello! Your name is {} and you are {} years old. You live in {} and you love {}.'
output = string.format(name, age, city, enjoy)

#Print output to screen:
print(output)


