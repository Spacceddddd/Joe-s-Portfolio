#Password Authenticator
"""
The password variable stores the input entered by the user.
Then the loop runs 5 times and if the password is correct, it prints, confirmed
"""
user_name = input("Enter your username: ")
password = input("Enter your new password: ")

for i in range(5):#This is a loop, for every incorrect entry, it breaks and restarts the loop 
    if user_name == password:#This ensures password and user names can't be the same
        print("Username and Password can't be the same")
        break
    x = input("Please reenter your password: ")#This asks the user to reenter their password
    if x == password:
        print(f"Password confirmed! \nWelcome {user_name}")#This confirms if the entry is correct and welcomes the user
        break
    else:
        print("Wrong password, try again.")#This occurs when the entry is incorrect
else:
    print("Too many failed attempts. Try again later.")#This occurs outside the loop to make sure that when the loop ends, it stops the user
