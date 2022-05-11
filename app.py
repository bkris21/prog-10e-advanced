from flask import Flask, request
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


class User:
    def __init__(self, username, email):
        self.id = None
        self.username = username
        self.email = email

    def to_dictionary(self):
        return {"id":self.id,"username":self.username,"email":self.email}


class UserService:
    id_genrator = 1

    def __init__(self):
        self.users = []

    def add_user(self,user):
        user.id = UserService.id_genrator
        self.users.append(user)
        UserService.id_genrator+=1

user_service = UserService()


@app.route('/users', methods = ['GET'])
def get_all_users():
    my_list = []
    for item in user_service.users:
        my_list.append(item.to_dictionary())
    
    return json.dumps(my_list)

if __name__ == '__main__':
    user_service.add_user(User("asd","asd@gmail.com")) 
    user_service.add_user(User("vsd","vsd@gmail.com"))
    app.run()