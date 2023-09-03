from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
from flask_cors import CORS

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app, resources={r'/*': {'origins': '*'}})

#db initialization
db = SQLAlchemy(app)
ma = Marshmallow(app)
app.app_context().push()

#db setup
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(35))
    gender = db.Column(db.String(10))

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'gender')
        
user_schema = UserSchema()
users_schema = UserSchema(many=True)

USERS = [
    {
        'id': 1,
        'name': 'John',
        'gender': 'male'
    },
     {
        'id': 2,
        'name': 'Mark',
        'gender': 'male'
    },
      {
        'id': 3,
        'name': 'Sarah',
        'gender': 'Female'
    },
    {
        'id': 4,
        'name': 'Kate',
        'gender': 'Female'
    }
]

#add user 
@app.route('/users', methods=['GET', 'POST'])
def getall_users():
    response_object = {'status': 'success'}
    if request.method == 'POST':
          post_data = request.get_json()
          USERS.append({
                'id': post_data.get('id'),
                'name': post_data.get('name'),
                'gender': post_data.get('gender')
          })
          name = request.json['name']
          gender = request.json['gender']
          new_user = User(name, gender)
          db.session.add(new_user)
          db.session.commit()
          response_object['message'] = 'User added!'
    else:
          response_object['users'] = USERS
          
    return jsonify(response_object)
  

#get users list
@app.route('/user', methods=['GET'])
def get_users():
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    return jsonify(result)

#get single user by id
@app.route('/user/<id>', methods=['GET'])
def get_user(id):
    user = User.query.get(id)
    return user_schema.jsonify(user)

#edit user
@app.route('/user/<id>', methods=['PUT'])
def edit_user(id):
    user = User.query.get(id)
    
    name = request.json['name']
    gender = request.json['gender']
    
    user.name = name
    user.gender = gender
    
    db.session.commit()
    
    return user_schema.jsonify(user)

if __name__ == '__main__':
    app.run()
    
