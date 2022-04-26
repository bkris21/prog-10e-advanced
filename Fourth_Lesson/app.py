from flask import Flask, redirect, url_for, request
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
        return {"id":self.id,"username": self.username, "email": self.email}

class UserService:

    id_generator = 1
   
    def __init__(self):
        self.users = []

    def add_user(self,user):
        user.id = UserService.id_generator
        self.users.append(user)
        UserService.id_generator += 1

    
user_service = UserService()

@app.route('/users/<id>', methods = ['GET'])
def get_user_by_id(id):
    for item in user_service.users:
        if item.id == int(id):
            print("ok")
            return json.dumps(item.to_dictionary())
  
@app.route('/users', methods = ['GET'])
def get_all_users():
    my_list = []
    for item in user_service.users:
        my_list.append(item.to_dictionary())

    return json.dumps(my_list)

@app.route('/users', methods = ['POST'])
def add_new_user():
   request_dict = request.get_json()
   user_service.add_user(User(request_dict["name"],request_dict["email"]))
   return json.dumps({"message": "ok"})

@app.route('/users/<id>', methods=['DELETE'])
def delete_user_by_id(id):
      for item in user_service.users:
        if item.id == int(id):
            user_service.users.remove(item)
      return "deleted"   

if __name__ == '__main__':
    user_service.add_user(User("jdks","asd@gmail.com"))
    app.run()