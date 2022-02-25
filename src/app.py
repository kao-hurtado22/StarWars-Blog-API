from flask import Flask, jsonify, request, json
from flask_migrate import Migrate
from models import db, User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (JWTManager, create_access_token, get_jwt_identity, jwt_required)
import datetime

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///dev_4geeks.db"
app.config['JWT_SECRET_KEY'] = ''

db.init_app(app)
Migrate(app, db)
jwt = JWTManager(app)


@app.route('/users', methods=['GET', 'POST'])
@app.route('/users/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def users(id = None):
    if request.method == 'GET':
        if id is not None:
            user = User.query.get(id)
            if not user: return jsonify({ "msg": "User not found!"}), 404
            return jsonify(user.serilize()), 200
        else:
            users = User.query.all()
            users = list(map(lambda user: user.serialize(), users))
            return jsonify(users), 200


    if request.method == 'POST':
       
        name = request.json.get('name')
        lastname = request.json.get('lastname')
        specie = request.json.get('specie', "")
        homeworld = request.json.get('homeworld', "")
        gender = request.json.get('gender', "")
        

        if not name: return jsonify({ "msg": "Name is required!"}), 400
        if not lastname: return jsonify({ "msg": "Lastname is required!"}), 400

        user = User() 
        user.name = name
        user.lastname = lastname

        profile = Profile()
        profile.specie = specie
        profile.homeworld = homeworld
        profile.gender = gender   

        user.profile = profile
        user.save()

        return jsonify(user.serialize()), 201

    if request.method == 'PUT':
     
        name = request.json.get('name') 
        lastname = request.json.get('lastname')
        specie = request.json.get('specie', "")
        homeworld = request.json.get('homeworld', "")
        gender = request.json.get('gender', "")

        if not name: return jsonify({ "msg": "Name is required!"}), 400
        if not lastname: return jsonify({ "msg": "Lastname is required!"}), 400

        user = User.query.get(id) 

        if not user: return jsonify({ "msg": "User not found!"}), 404

        user.name = name
        user.lastname = lastname
        user.profile.specie = specie
        user.profile.world = world
        user.profile.gender = gender
        user.update()

        return jsonify(user.serialize()), 200

        """ Columna de Planets """

    if request.method == 'POST':
       
        name = request.json.get('name')
        terrain = request.json.get('terrain')
        climate = request.json.get('climate')
        gravity = request.json.get('gravity')
        
        if not name: return jsonify({ "msg": "Name is required!"}), 400

        user = User() 
        user.name = name

        profile = Profile()
        profile.terrain = terrain
        profile.climate = climate
        profile.gravity = gravity
         
        user.profile = profile
        user.save()

        return jsonify(user.serialize()), 201

    if request.method == 'PUT':
     
        name = request.json.get('name')
        terrain = request.json.get('terrain')
        climate = request.json.get('climate')
        gravity = request.json.get('gravity')

        if not name: return jsonify({ "msg": "Name is required!"}), 400

        user = User.query.get(id) 

        if not user: return jsonify({ "msg": "User not found!"}), 404

        user.name = name
        user.terrain = terrain
        user.profile.climate = climate
        user.profile.gravity = gravity
        user.update()

        return jsonify(user.serialize()), 200


        """ columna starships """

    if request.method == 'POST':
       
        name = request.json.get('name')
        model = request.json.get('model')
        manufacturer = request.json.get('manufacturer')
        starship_class = request.json.get('starship_class') 

        if not name: return jsonify({ "msg": "Name is required!"}), 400

        user = User() 
        user.name = name

        profile = Profile()
        profile.model = model
        profile.manufacturer = manufacturer
        profile.starship_class = starship_class

        user.profile = profile
        user.save()

        return jsonify(user.serialize()), 201

    if request.method == 'PUT':
     
        name = request.json.get('name')
        model = request.json.get('model')
        manufacturer = request.json.get('manufacturer')
        starship_class = request.json.get('starship_class')

        if not name: return jsonify({ "msg": "Name is required!"}), 400

        user = User.query.get(id) 

        if not user: return jsonify({ "msg": "User not found!"}), 404

        user.name = name
        user.profile.model = model
        user.profile.manufacturer = manufacturer
        user.profile.starship_class = starship_class
        user.update()

        return jsonify(user.serialize()), 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3452)