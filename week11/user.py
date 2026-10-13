"""
# Attributes
# username
# gender
# bio

email
password
age -> date of birth

# Behaviours
- log in
- add friend

# - make a post
# - like ???
# - comment
"""
import datetime

class User:
    MINIMUM_AGE = 13

    def __init__(self, email, date_of_birth, password):
        self.email = email
        self.__date_of_birth = date_of_birth
        self.__password = password
        self.friends = []

    def get_password(self):
        return self.__password

    def set_date_of_birth(self, date_of_birth):
        years = datetime.datetime(date_of_birth).year - datetime.datetime.now().year
        if years < User.MINIMUM_AGE:
            print("You're too young")
        else:
            self.__date_of_birth = date_of_birth

    def set_password(self, password):
        if len(password) < 8:
            print("Password should have at least 8 characters")
        else:
            self.__password = password

    def log_in(self, password):
        if password == self.__password:
            print("Logged in successfully")
            return True
        else:
            print("Unauthorised!")
            return False

    def add_friend(self, other_user):
        self.friends.append(other_user)