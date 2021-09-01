from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime

app = Flask(__name__)

app.config['SECRET_KEY']='MySecretKey'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///UserItems.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)   

class Users(db.Model):
   id = db.Column(db.Integer, primary_key=True, nullable=False)
   name = db.Column(db.String(50), unique=True, nullable=False)
   password = db.Column(db.String(50), nullable=False)

class Items(db.Model):  
   id = db.Column(db.Integer, primary_key=True, nullable=False)
   name = db.Column(db.String(50), unique=True, nullable=False)
   user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)

@app.route('/api/register', methods=['GET', 'POST'])
def signup_user():
   data = request.get_json()

   user_count = Users.query.filter_by(name=data['name']).count()
   if user_count > 0:
      return jsonify({'message': 'user already found'})   
      
   hashed_password = generate_password_hash(data['password'], method='sha256')
 
   new_user = Users(name=data['name'], password=hashed_password) 
   db.session.add(new_user)  
   db.session.commit()    

   return jsonify({'message': 'registered successfully'})   


@app.route('/api/login', methods=['GET', 'POST'])  
def login_user():
   auth = request.authorization

   if not auth or not auth.username or not auth.password:
      return make_response('could not verify', 401, {'WWW.Authentication': 'Basic realm: "login required"'})

   user = Users.query.filter_by(name=auth.username).first()
     
   if check_password_hash(user.password, auth.password):
      token = jwt.encode({'id': user.id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'], algorithm="HS256")

      return jsonify({'token' : token})

   return make_response('could not verify',  401, {'WWW.Authentication': 'Basic realm: "login required"'})

@app.route('/api/users', methods=['GET'])
def get_all_users():
   
   users = Users.query.all()

   result = []

   for user in users:
      user_data = {}  
      user_data['name'] = user.name
      user_data['password'] = user.password
       
      result.append(user_data)   

   return jsonify({'users': result})  


@app.route('/api/items', methods=['GET', 'POST'])
def get_items():
   try:
      token = request.get_json()['token']
   except:
      return jsonify({'message': 'a valid token is missing'})

   data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])

   items = Items.query.filter_by(user_id=data['id'])
   output = []  
   for item in items:   
      item_data = {}  
      item_data['id'] = item.id 
      item_data['user_id'] = item.user_id 

      item_data['name'] = item.name 

      output.append(item_data)  

   return jsonify({'list_of_items' : output})
   

@app.route('/api/item', methods=['POST', 'GET'])
def create_item():
   try:
      token = request.get_json()['token']
   except:
      return jsonify({'message': 'a valid token is missing'})
   name = request.get_json()['name']
   data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])   

   new_items = Items(name=name, user_id=data['id'])
   db.session.add(new_items)
   db.session.commit()

   return jsonify({'message' : 'new item created'})

@app.route('/api/itemdel', methods=['DELETE'])
def delete_item():
   try:
      token = request.get_json()['token']
   except:
      return jsonify({'message': 'a valid token is missing'})
   item_id = request.get_json()['id']      
   data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
   item = Items.query.filter_by(id=item_id, user_id=data['id']).first()
   if not item:
      return jsonify({'message': 'item does not exist'})

   db.session.delete(item)
   db.session.commit()

   return jsonify({'message': 'item deleted'})

@app.route('/api/send', methods=['POST', 'GET'])
def send_item():
   try:
      token = request.get_json()['token']
   except:
      return jsonify({'message': 'a valid token is missing'})
   data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
   sender_id=data['id']
   item_id = request.get_json()['item_id']
   user_id = request.get_json()['user_id']
   item = Items.query.filter_by(id=item_id).first()
   if item.user_id != user_id:
      return jsonify({'message' : "It is not your item"})

   item_token = jwt.encode({'sender_id': sender_id, 'user_id': user_id, 'item_id' : item_id}, app.config['SECRET_KEY'], algorithm="HS256")

   return jsonify({'item_token' : item_token})

@app.route('/api/receive', methods=['POST', 'GET'])
   
def receive_item():
   if request.method == 'POST':
      try:
         token = request.get_json()['token']
      except:
         return jsonify({'message': 'a valid token is missing'})
      try:
         item_token = request.get_json()['item_token']
      except:
         return jsonify({'message': 'a valid item_token is missing'})
   elif request.method == 'GET':
      try:
         token = request.args.get('token')
         item_token = request.args.get('item_token')
      except:
         return jsonify({'message': 'valid tokens are missing'})
   data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
   user_id=data['id']
   item_data = jwt.decode(item_token, app.config['SECRET_KEY'], algorithms=["HS256"])
   receiver_id=item_data['user_id']
   item_id=item_data['item_id']       

   if int(receiver_id) != int(user_id):
      return jsonify({'message' : 'Invalid receiver'})
   item = Items.query.filter_by(id=item_id).first()
   item.user_id = user_id
   db.session.commit()
   return jsonify({'message': 'item was transferred successfully'})


if  __name__ == '__main__':
   db.create_all()
   app.run(debug=True)
