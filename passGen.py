import hashlib
import os

class passGen:

    # initial construction: password and key are not yet defined, only the salt

    def __init__(self):
        self.password = None
        self.key = None
        self.salt = os.urandom(32)
        self.store = None

    def new(self):
        print("Enter a new password. The following requirements must be met:\n")
        print("1. At least one number")
        print("2. At least one uppercase AND one lowercase character.")
        print("3. One special symbol (@, #, $, %, -)")
        print("4. At least 8 characters in length. \n")
        p = input("Password: ")
        valid = False
        while not valid:
            result = self.validate(p)
            if result != "Valid":
                print("Password invalid: ", result)
                p = input("Password: ")
            else:
                valid = True
        self.key = hashlib.pbkdf2_hmac('sha256', p.encode('utf-8'), self.salt, 100000)
        self.store = self.salt + self.key

    def validate(self, passwd):
        specials = ['@', '$', '#', '%', '-']
        result = "Valid"

        if len(passwd) < 8:
            result = 'Length should be at least 8'
            return result
        elif not any(char.isdigit() for char in passwd):
            result = 'Password must contain at least one number'
            return result
        elif not any(char.isupper() for char in passwd):
            result = 'Password must contain at least one uppercase character'
            return result
        elif not any(char.islower() for char in passwd):
            result = 'Password must contain at least one lowercase character'
            return result
        elif not any(char in specials for char in passwd):
            result = 'Password must contain at least one special character'
            return result
        return result