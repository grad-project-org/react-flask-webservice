from flask import Flask, jsonify, request
from datetime import datetime
from flask_cors import cross_origin
from cnx import DataBase
from flask_jwt_extended import JWTManager
from flask_jwt_extended import (create_access_token)


app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdasdasdfasfaasdf'


@app.route('/user/login', methods=['POST'])
@cross_origin()
def login():
    try:

        entry = request.get_json()
        correo = entry['email']
        clave = entry['password']
        db = DataBase()
        res = db.get_user(correo, clave)
        db.close()
        return jsonify(res)

    except Exception as e:
        error = {
            "status": 400,
            "description": f"Endpoint error {e}"
        }

        return jsonify(error)


@app.route('/users/register', methods=['POST'])
@cross_origin()
def register_users():
    try:
        entry = request.get_json()

        first_name = entry['first_name']
        last_name = entry['last_name']
        password = entry['password']
        email = entry['email']
        db = DataBase()
        res = db.user_register(first_name, last_name, email, password)
        db.close()
        return jsonify(res)
    except Exception as e:

        error = {
            "status": 400,
            "description": f"Endpoint error {e}"
        }

        return jsonify(error)


if __name__ == '__main__':

    app.run(host="localhost", port=5000, debug=True)
