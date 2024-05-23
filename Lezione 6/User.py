class User:
    def __init__(self, first_name, last_name, age, height, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height
        self.login_attempts = login_attempts
    def describe_user(self):
        print(f"Name: {self.first_name},Last name: {self.last_name}, Age: {self.age},Height: {self.height}")

    def greet_user(self):
        print(f"Good morning {self.first_name}")
    
    def increment_login_attempts(self):
        self.login_attempts = self.login_attempts + 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

class Privileges():
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print(self.privileges)

class Admin(User):
    def __init__(self, first_name, last_name, age, height, login_attempts, privileges:Privileges):
        super().__init__(first_name, last_name, age, height, login_attempts)
        self.privileges = privileges
