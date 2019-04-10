# Ask user for their email address:
email = input('Please enter your email: ').strip().lower()  

#slice out the user name:
user_name = email[:email.index('@')]

#slice the doamin name:
domain_name = email[email.index('@')+1:]


#format message:
message = 'your user name address is : {} and your domain name is: {}'.format(user_name, domain_name)


# display the messasge:
print(message) 
