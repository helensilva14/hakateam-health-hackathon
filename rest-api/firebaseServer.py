import firebase_admin
from firebase_admin import db
import flask
from flask_restful import Api
from resources.consultation import ConsultationsResource, ConsultationResource

app = flask.Flask(__name__)
api = Api(app)

api.add_resource(ConsultationsResource, '/consultations')
api.add_resource(ConsultationResource, '/consultations/<string:id>')

DOCTORS = db.reference('doctors')
PATIENTS = db.reference('patients')
CONSULTATIONS = db.reference('consultations')

SUPERHEROES = db.reference('superheroes')

@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = SUPERHEROES.get()
    return flask.jsonify(heroes)

@app.route('/heroes', methods=['POST'])
def create_hero():
    req = flask.request.json
    hero = SUPERHEROES.push(req)
    return flask.jsonify({'id': hero.key}), 201

@app.route('/heroes/<id>')
def read_hero(id):
    return flask.jsonify(_ensure_hero(id))

@app.route('/heroes/<id>', methods=['PUT'])
def update_hero(id):
    _ensure_hero(id)
    req = flask.request.json
    SUPERHEROES.child(id).update(req)
    return flask.jsonify({'success': True})

@app.route('/heroes/<id>', methods=['DELETE'])
def delete_hero(id):
    _ensure_hero(id)
    SUPERHEROES.child(id).delete()
    return flask.jsonify({'success': True})

def _ensure_hero(id):
    hero = SUPERHEROES.child(id).get()
    if not hero:
        flask.abort(404)
    return hero

if __name__ == '__main__':
    app.run(host='127.0.0.1',debug=True)