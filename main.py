from passGen import passGen

test = passGen()
valid = test.verify()
while not valid:
    print('Password was incorrect.')
    valid = test.verify()

print('Password verified')