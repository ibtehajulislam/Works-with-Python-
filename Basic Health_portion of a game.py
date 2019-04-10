import random 

#Create the primary health
health = 50
difficulty = 2 #Easy Mode


#Generating a random number as life portion
potion_health = int(random.randint(25,50)/difficulty)

health = health + potion_health

print(health)

 
