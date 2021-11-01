import hashlib
import os

class passGen:

    # initial construction: password and key are not yet defined, only the salt

    def __init__(self, status, store):
        if status == 0:
            self.key = None
            self.salt = os.urandom(32)
            self.store = None
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
        else:
            self.store = store
            self.key = self.store[32:]
            self.salt = self.store[:32]

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

    def verify(self):
        passwd = input("Enter your password: ")
        new_key = hashlib.pbkdf2_hmac('sha256', passwd.encode('utf-8'), self.store[:32], 100000)
        if new_key == self.store[32:]:
            return True
        else:
            return False