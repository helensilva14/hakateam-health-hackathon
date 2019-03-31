# import firebase_admin
# from firebase_admin import credentials, db
import flask
from flask_restful import Api

import resources.endpoints as endpoints

app = flask.Flask(__name__)
api = Api(app)

# add the resources to the API specifying the base URL endpoints
api.add_resource(endpoints.ConsultationsResource, '/api/consultations')
api.add_resource(endpoints.ConsultationResource, '/api/consultations/<string:id>')
api.add_resource(endpoints.DoctorsResource, '/api/doctors')
api.add_resource(endpoints.DoctorResource, '/api/doctors/<string:id>')
api.add_resource(endpoints.PatientsResource, '/api/patients')
api.add_resource(endpoints.PatientResource, '/api/patients/<string:id>')

if __name__ == '__main__':
    app.run(host='127.0.0.1',debug=True)