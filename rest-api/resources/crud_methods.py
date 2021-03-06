import flask

"""
Creates entities using the specified database on Firebase
"""
def create_entity(DATABASE):
    req = flask.request.json
    ids = list()
    for item in req:
        item = DATABASE.push(item)
        ids.append({'id': item.key})
    response = flask.jsonify(str(ids))
    response.status_code = 201
    return response

"""
Gets the entities using the specified database on Firebase
"""
def get_data(DATABASE): 
    response = flask.jsonify(DATABASE.get())
    response.status_code = 200
    return response

"""
Gets an entity using the specified database on Firebase
"""
def get_entity(DATABASE, id):
    entity = DATABASE.child(id).get()
    if not entity:
        flask.abort(404)
    return entity

"""
Deletes an entity using the specified database on Firebase
"""
def delete_entity(DATABASE, id):
    get_entity(DATABASE, id)
    DATABASE.child(id).delete()
    response = flask.jsonify({'msg': 'Succesfully deleted'})
    response.status_code = 204
    return response

"""
Updates an entity using the specified database on Firebase
"""
def update_entity(DATABASE, id):
    get_entity(DATABASE, id)
    req = flask.request.json
    DATABASE.child(id).update(req)
    response = flask.jsonify({'success': 'Succesfully updated'})
    response.status_code = 200
    return response
    