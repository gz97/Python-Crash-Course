class User:
    def __init__(self, first_name, last_name, user_name, age, city):
        self.first_name = first_name
        self.last_name = last_name 
        self.user_name = user_name
        self.age = age
        self.city = city 
        self.login_attempts = 0

    def describe_user(self):
        print(f"User {self.user_name} is called {self.first_name.title()} {self.last_name. title()}.")
        print(f"User {self.user_name} is {self.age} years old and comes from {self.city. title()}.")

    def greet_user(self):
        print(f"Hello {self.user_name}.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(User):
    def __init__(self, first_name, last_name, user_name, age, city):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(first_name, last_name, user_name, age, city)
        self.privileges = Privileges()


class Privileges:
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("- This user has no privileges.")