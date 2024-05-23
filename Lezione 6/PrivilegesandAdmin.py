from User_1 import *

class Privileges():
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print(self.privileges)

class Admin(User):
    def __init__(self, first_name, last_name, age, height, login_attempts, privileges:Privileges):
        super().__init__(first_name, last_name, age, height, login_attempts)
        self.privileges = privileges