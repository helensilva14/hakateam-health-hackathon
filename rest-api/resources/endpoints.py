import firebase_admin
from firebase_admin import db

import requests
import flask
from flask_restful import Resource

from resources.crud_methods import create_entity, get_data, get_entity, update_entity, delete_entity    

firebase_admin.initialize_app(options={
    'databaseURL': 'https://hakateam2019.firebaseio.com/'})

DOCTORSTORS = db.reference('doctors')
CONSULTATIONS = db.reference('consultations')
PATIENTS = db.reference('patients')

class ConsultationsResource(Resource):
    def get(self):
        return get_data(CONSULTATIONS)

    def post(self):
        return create_entity(CONSULTATIONS)

class ConsultationResource(Resource):
    def get(self, id):
        return get_entity(CONSULTATIONS, id) 

    def put(self, id):
        return update_entity(CONSULTATIONS, id) 

    def delete(self, id):
        return delete_entity(CONSULTATIONS, id)

class DoctorsResource(Resource):
    def get(self):
        return get_data(DOCTORS)

    def post(self):
        return create_entity(DOCTORS)

class DoctorResource(Resource):
    def get(self, id):
        return get_entity(DOCTORS, id)

    def put(self, id):
        return update_entity(DOCTORS, id)

    def delete(self, id):
        return delete_entity(DOCTORS, id)

class PatientsResource(Resource):
    def get(self):
        return get_data(PATIENTS)

    def post(self):
        return create_entity(PATIENTS)

class PatientResource(Resource):
    def get(self, id):
        return get_entity(PATIENTS, id)

    def put(self, id):
        return update_entity(PATIENTS, id)

    def delete(self, id):
        return delete_entity(PATIENTS, id)

class DoctorsRecommendation(Resource):
    def post(self):
        req = flask.request.json

        # create a consultation object containing the patient data and the selected specialty
        url = ''
        headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
        # predictions = requests.post(url, data=j_data, headers=headers)
        # ids.append({'id': item.key})
            
        # response = flask.jsonify(str(ids))
        # response.status_code = 201
        # return response

        # j_data = json.dumps(mock_data)

        # print(r, r.text) # print(r.json())