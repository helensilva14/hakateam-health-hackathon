import numpy as np
from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

@app.route("api/patient/<int:id>/consultations/", methods=['POST'])
def create_consultation(id):
    

@app.route('/api',methods=['POST'])
def predict():
    # get the data from the POST request
    data = request.get_json(force=True)

    # make prediction using model loaded from disk as per the data.
    prediction = model.predict([[np.array(data['exp'])]])

    # take the first value of prediction
    output = prediction[0]

if __name__ == '__main__':
	modelfile = '../models/PatientModel.pkl'    
	model = pickle.load(open(modelfile, 'rb'))
	print("== Model loaded ==")
	app.run(port=5000,debug=True)