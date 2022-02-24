from API.guitares import *

# route to get all movies
@app.route('/guitares', methods=['GET'])
def get_guitares():
    '''Function to get all the guitares in the database'''
    return jsonify(Guitare.get_all_guitares())


# route to get guitare by id
@app.route('/guitares/<int:id>', methods=['GET'])
def get_guitare_by_id(id):
    return_value = Guitare.get_guitare(id)
    return jsonify(return_value)


# route to add new guitare
@app.route('/guitares', methods=['POST'])
def add_guitare():
    '''Function to add new guitare to our database'''
    request_data = request.get_json()  # getting data from client
    Guitare.add_guitare(request_data["nom"], request_data["prix"],
                    request_data["nbr_ventes"])
    response = Response("Guitare added", 201, mimetype='application/json')
    return response


# route to update guitare with PUT method
@app.route('/guitares/<int:id>', methods=['PUT'])
def update_guitare(id):
    '''Function to edit guitare in our database using movie id'''
    request_data = request.get_json()
    Guitare.update_guitare(id, request_data['nom'], request_data['prix'],request_data['nbr_ventes'])
    response = Response("Guitare Updated", status=200, mimetype='application/json')
    return response


# route to delete movie using the DELETE method
@app.route('/guitares/<int:id>', methods=['DELETE'])
def remove_guitare(id):
    '''Function to delete guitare from our database'''
    Guitare.delete_guitare(id)
    response = Response("Guitare Deleted", status=200, mimetype='application/json')
    return response


if __name__ == "__main__":
    app.run(port=1234, debug=True)