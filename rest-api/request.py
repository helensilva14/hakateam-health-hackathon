import json
import requests

url = 'http://localhost:5000/api'

mock_data = [
    {
        medicalConsultationId: 1,
        state: 'SP',
        dateOfService: '4/25/2018'
    }
]

j_data = json.dumps(mock_data)

headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=j_data, headers=headers)
print(r, r.text) # print(r.json())