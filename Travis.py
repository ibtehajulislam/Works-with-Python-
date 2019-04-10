known_users = ['Alice', 'Bob', 'Clarie', 'Dan', 'Emma', 'Fred', 'Georgie', 'Harry']

while True:
    print('Hi! My name is Travis')
    name = input('What is your name?: ').strip().capitalize() 


    if name in known_users:
        print('Hello {}!'.format(name))
        remove = input('Would you like to be removed from the system (y/n)?: ').lower()

        if remove == 'y':
            known_users.remove(name)
            
        elif remove == 'n':
            print('No problem. I didnt want you to leave anyway.')
        
    else:
        print('Hmmm! I dont think i met you {}'.format(name))
        add_me = input('Would you like to be added into the system?: (y/n)').lower().strip()

        if add_me == 'y':
            known_users.append(name)
            print('Welcome {} to the system.'.format(name))
            
        elif add_me == 'n':
            print('No worries! See you around!')
    