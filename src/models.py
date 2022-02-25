from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'
    id =db.Column(db.Integer, primary_key=True)
    email =  db.Column(db.String(100), unique=True, nullable=False)
    password =  db.Column(db.String(100), nullable=False)
    characters = db.relationship('Characters', backref='user', uselist=False)

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "password": self.password,
            "characters": self.characters.serialize()
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Characters(db.Model):
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text(), default="")
    lastname = db.Column(db.Text(), default="")
    specie =db.Column(db.Text(), default="")
    homeworld = db.Column(db.Text(), default="")
    gender = db.Column(db.Text(), default="")
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    favorites_characters = db.relationship('favorites_characters', backref='characters', uselist=False)
    
    def serialize(self):
        return {
            "id": self.id,
            "email": self.user.email,
            "lastname": self.lastname,
            "specie": self.specie,
            "world": self.world,
            "gender": self.gender,
            "favorites_characters": self.favorites_characters.serialize()
        }

class Favorites_characters(db.Model):
    __tablename__ = 'favorites_characters'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    characters_id = db.Column(db.Integer, db.ForeignKey('characters.id'), nullable=False)

    def serialize(self):
        return {
            "id": self.id
        }

class Planets(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    terrain = db.Column(db.String(100), nullable=False)
    climate = db.Column(db.String(100), nullable=False)
    gravity = db.Column(db.String(100), nullable=False)
    favorites_planets = db.relationship('favorites_planets', backref='planets', uselist=False)

    def serialize(self):
        return {
            "id": self.id,
            "world": self.world,
            "lenguage": self.lenguage,
            "favorites_plantes": self.favorites_planets.serialize()
        }

class Favorites_planets(db.Model):
    __tablename__ = 'favorites_planets'
    id =db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    planets_id = db.Column(db.Integer, db.ForeignKey('planets.id'), nullable=False)

    def serialize(self):
        return {
            "id": self.id
        }

class Starships(db.Model):
    __tablename__ = 'starships'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    model = db.Column(db.String(100), nullable=False)
    manufacturer = db.Column(db.String(100), nullable=False)
    starship_class = db.Column(db.String(100), nullable=False)
    favorites_starships = db.relationship('favorites_starships', backref='starships', uselist=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "manufacturer": self.manufacturer,
            "starship_class": self.starship_class,
            "favorites_starships": self.favorites_starships.serialize()
        }

class Favorites_starships(db.Model):
    __tablename__ = 'favorites_starships'
    id = db.Column(db.Integer, primary_key=True)
    user_id =db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    starships_id = db.Column(db.Integer, db.ForeignKey('starships.id'), nullable=False)

    def serialize(self):
        return {
            "id": self.id
        }



