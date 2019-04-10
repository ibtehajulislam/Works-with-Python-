#Creating a list of Cinemas
films = {
            "Finding Dory": [3,5],
            "Bourne": [18,5],
            "Tarzan": [15,1],
            "Ghost Buster": [12,5]
    }

while True:
#Asking user to choose the cinema of their choice from the list    
    choice = input('What film would you like to watch?: ').strip().title()
    if choice in films:
        age = int(input("How old are you?: ").strip())

        ## check user's age:
        if age >= films[choice][0]:

            #Check enough seats:
            num_seats = films[choice][1]
            if num_seats > 0:
                print("Enjoy the film.")
                films[choice][1] = films[choice][1] - 1
            else:
                print("Sorry! We are sold out.")
        else:
            print("You are too young to watch this film.")
        
    else:
        print("Sorry! We don't have this film.")
    
