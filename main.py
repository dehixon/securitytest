from passGen import passGen

test = passGen(0, None)
valid = test.verify()
while not valid:
    print('Password was incorrect.')
    valid = test.verify()

print('Password verified')
file = open("passwords.txt", "wb")
file.write(test.store + b'\n')
file.write(test.store + b'\n')
file.close()
print("File written")