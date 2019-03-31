import firebase_admin
from firebase_admin import db

import requests
import flask
from flask_restful import Resource

from resources.crud_methods import create_entity, get_data, get_entity, update_entity, delete_entity    

firebase_admin.initialize_app(options={'databaseURL': 'FIREBASE_DATABASE_URL'})

"""
Get the databases from the remote server (Firebase)
"""
DOCTORS = db.reference('doctors')
CONSULTATIONS = db.reference('consultations')
PATIENTS = db.reference('patients')

"""
Endpoints for consultations
"""
class ConsultationsResource(Resource):
    def get(self):
        return get_data(CONSULTATIONS)

    def post(self):
        return create_entity(CONSULTATIONS)

"""
Endpoints for a given consultation
"""
class ConsultationResource(Resource):
    def get(self, id):
        return get_entity(CONSULTATIONS, id) 

    def put(self, id):
        return update_entity(CONSULTATIONS, id) 

    def delete(self, id):
        return delete_entity(CONSULTATIONS, id)

"""
Endpoints for doctors
"""
class DoctorsResource(Resource):
    def get(self):
        return get_data(DOCTORS)

    def post(self):
        return create_entity(DOCTORS)

"""
Endpoints for a given doctor
"""
class DoctorResource(Resource):
    def get(self, id):
        return get_entity(DOCTORS, id)

    def put(self, id):
        return update_entity(DOCTORS, id)

    def delete(self, id):
        return delete_entity(DOCTORS, id)

"""
Endpoints for patients
"""
class PatientsResource(Resource):
    def get(self):
        return get_data(PATIENTS)

    def post(self):
        return create_entity(PATIENTS)

"""
Endpoints for a given patient
"""
class PatientResource(Resource):
    def get(self, id):
        return get_entity(PATIENTS, id)

    def put(self, id):
        return update_entity(PATIENTS, id)

    def delete(self, id):
        return delete_entity(PATIENTS, id)

"""
Endpoints about the doctos recommendation
"""
class DoctorsRecommendation(Resource):
    def post(self):
        # get the selected specialty and city
        req = flask.request.json

        """
        [TODO] Here will occur the integration between the API and the AI model
        """
        # create a consultation object appending the patient data

        # specify the model endpoint
        url = 'http://localhost:4646/api/recommend-doctors'
        headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}

        # send request to get the doctors recommendations
        response = requests.post(url, data=req, headers=headers)
        response.status_code = 200
        return response
