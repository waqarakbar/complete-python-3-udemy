import pymongo
from pymongo import MongoClient
import bcrypt

class UserModel:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.code_wizards
        self.Users = self.db.users

    def create_user(self, data):
        hashed_pw = bcrypt.hashpw(data.password.encode(), bcrypt.gensalt())
        user_data = {
            'username': data.username,
            'fullname': data.fullname,
            'email': data.email,
            'password': hashed_pw
        }
        id = self.Users.insert(user_data)
        print('uid is ', id)

    def check_user(self, data):
        user = self.Users.find_one({'username': data.username})
        if user:
            if bcrypt.checkpw(data.password.encode(), user["password"]):
                return user
            else:
                return False
        else:
            return False
