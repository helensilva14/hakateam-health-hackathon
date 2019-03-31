# import firebase_admin
# from firebase_admin import credentials, db
      
# firebase_admin.initialize_app(options={
#     'databaseURL': 'https://hakateam2019.firebaseio.com/'})

# DOCTORS = db.reference('doctors')
# CONSULTATIONS = db.reference('consultations')

import flask
from flask_restful import Api

from resources.consultation import ConsultationsResource, ConsultationResource, DoctorResource, DoctorsResource

# DOC = db.reference('doctors')
# CON = db.reference('consultations')

#firebase_admin.initialize_app()

# firebase_admin.initialize_app(name="app", options={
#     'databaseURL': 'https://hakateam2019.firebaseio.com/'
# })

app = flask.Flask(__name__)
api = Api(app)

api.add_resource(ConsultationsResource, '/consultations')
api.add_resource(ConsultationResource, '/consultations/<string:id>')
api.add_resource(DoctorsResource, '/doctors')
api.add_resource(DoctorResource, '/doctors/<string:id>')

if __name__ == '__main__':
    app.run(host='127.0.0.1',debug=True)