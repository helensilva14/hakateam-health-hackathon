import firebase_admin
from firebase_admin import db
import flask

from flask_restful import Resource

firebase_admin.initialize_app(options={
    'databaseURL': 'https://hakateam2019.firebaseio.com/'
})

DATABASE = db.reference('consultations')

def _get_instance(id):
    item = DATABASE.child(id).get()
    if not item:
        flask.abort(404)
    return item

class ConsultationsResource(Resource):
    def get(self):
        return flask.jsonify(DATABASE.get())

    def post(self):
        req = flask.request.json
        item = DATABASE.push(req)
        response = flask.jsonify({'id': item.key})
        response.status_code = 201
        return response

class ConsultationResource(Resource):
    def get(self, id):
        return flask.jsonify(_get_instance(id))

    def put(self, id):
        _get_instance(id)
        req = flask.request.json
        DATABASE.child(id).update(req)
        response = flask.jsonify({'success': 'Succesfully updated'})
        response.status_code = 200
        return response

    def delete(self, id):
        _get_instance(id)
        DATABASE.child(id).delete()
        response = flask.jsonify({'msg': 'Succesfully deleted'})
        response.status_code = 204
        return response