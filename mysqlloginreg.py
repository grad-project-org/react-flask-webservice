from flask import Flask, jsonify, request, json
# from flask_mysqldb import MySQL
from datetime import datetime
from flask_cors import CORS, cross_origin
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_jwt_extended import (create_access_token)

app = Flask(__name__)

# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DB'] = 'nodejs_login1'
# app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
# app.config['JWT_SECRET_KEY'] = 'secret'

# mysql = MySQL(app)
# bcrypt = Bcrypt(app)
# jwt = JWTManager(app)

# CORS(app)

# @app.route('/users/register', methods=['POST'])
# @cross_origin()
# def register():
#     try:

#         entry = get_json()

        
#     except expression as identifier:
#         pass
#     # cur = mysql.connection.cursor()
#     first_name = request.get_json()['first_name']
#     last_name = request.get_json()['last_name']
#     email = request.get_json()['email']
#     password = bcrypt.generate_password_hash(request.get_json()['password']).decode('utf-8')
#     created = datetime.utcnow()
	
#     cur.execute("INSERT INTO users (first_name, last_name, email, password, created) VALUES ('" + 
# 		str(first_name) + "', '" + 
# 		str(last_name) + "', '" + 
# 		str(email) + "', '" + 
# 		str(password) + "', '" + 
# 		str(created) + "')")
#     mysql.connection.commit()
	
#     result = {
# 		'first_name' : first_name,
# 		'last_name' : last_name,
# 		'email' : email,
# 		'password' : password,
# 		'created' : created
# 	}

#     return jsonify({'result' : result})
	

# @app.route('/users/login', methods=['POST'])
# def login():
#     cur = mysql.connection.cursor()
#     email = request.get_json(force=True)['email']
#     password = request.get_json(force=True)['password']
#     result = ""
	
#     cur.execute("SELECT * FROM users where email = '" + str(email) + "'")
    
#     rv = cur.fetchone()
	
#     if  bcrypt.check_password_hash(rv['password'], password):
#         access_token = create_access_token(identity = {'first_name': rv['first_name'],'last_name': rv['last_name'],'email': rv['email']})
#         result = access_token
#     else:
#         result = jsonify({"error":"Invalid username and password"})
    
#     return result

@app.route('/user/login', methods=['POST'])
@cross_origin()
def login():
    try:

        
    except Exception as e:
        error = {
            "status":400, 
            "description":f"Endpoint error {e}"
        }
        return jsonify(error)



if __name__ == '__main__':
    app.run(debug=True)