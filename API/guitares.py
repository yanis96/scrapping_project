from settings import *
import json

# Initializing our database
db = SQLAlchemy(app)


# the class Movie will inherit the db.Model of SQLAlchemy
class Guitare(db.Model):
    __tablename__ = 'guitare'  # creating a table name
    id = db.Column(db.Integer, primary_key=True)  # this is the primary key
    nom = db.Column(db.String(80), nullable=False)
    # nullable is false so the column can't be empty
    prix = db.Column(db.Integer, nullable=False)
    nbr_ventes = db.Column(db.Integer, nullable=False)


    def json(self):
        return {'id': self.id, 'nom': self.nom,
                'prix': self.prix, 'nbr_ventes': self.nbr_ventes}
        # this method we are defining will convert our output to json

    @staticmethod
    def add_guitare(_nom, _prix, _nbr_ventes):
        '''function to add guitare to database using _nom, _prix, _nbr_ventes
        as parameters'''
        # creating an instance of our Movie constructor
        new_guitare = Guitare(nom=_nom, prix=_prix, nbr_ventes=_nbr_ventes)
        db.session.add(new_guitare)  # add new guitare to database session
        db.session.commit()  # commit changes to session

    @staticmethod
    def get_all_guitares():
        '''function to get all guitares in our database'''
        return [Guitare.json(movie) for movie in Guitare.query.all()]

    @staticmethod
    def get_guitare(_id):
        '''function to get movie using the id of the movie as parameter'''
        return [Guitare.json(Guitare.query.filter_by(id=_id).first())]
        # Guitare.json() coverts our output to the json format defined earlier
        # the filter_by method filters the query by the id
        # since our id is unique we will only get one result
        # the .first() method will get that first value returned

    @staticmethod
    def update_guitare(_id, _nom, _prix, _nbr_ventes):
        '''function to update the details of a guitare using the id, nom,
        prix and nbr_ventes as parameters'''
        guitare_to_update = Guitare.query.filter_by(id=_id).first()
        guitare_to_update.nom = _nom
        guitare_to_update.prix = _prix
        guitare_to_update.nbr_ventes = _nbr_ventes
        db.session.commit()

    @staticmethod
    def delete_guitare(_id):
        '''function to delete a guitare from our database using
        the id of the guitare as a parameter'''
        Guitare.query.filter_by(id=_id).delete()
        # filter guitare by id and delete
        db.session.commit()  # commiting the new change to our database
