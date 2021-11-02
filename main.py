from passGen import passGen

users = {}
print('Welcome to the password system.')
print('Enter 1 to login, 2 to create a new user, 3 to change password, 4 to delete a user, or 0 to exit.')
choice = input('Your choice: ')
if choice == 1:
    user = input('Enter your username: ')
    found = False
    counter = 0
    for k in users.keys():
        if user == k:
            print('User ' + user + ' found.')
            found = True
            break
        elif counter < len(users):
            counter + 1