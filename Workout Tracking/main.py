import requests
from datetime import datetime
import os

GENDER = 'male'
WEIGHT_KG = 83
HEIGHT_KG = 174
AGE = 30

API_ID = os.environ['API_ID']
API_KEY = os.environ['API_KEY']

exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

exercise_text = input('Tell me which exercises you did: ')

headers = {
    'x-app-id': API_ID,
    'x-app-key': API_KEY
}

parameters = {
    'query': exercise_text,
    'gender': GENDER,
    'weight_kg': WEIGHT_KG,
    'height_cm': HEIGHT_KG,
    'age': AGE
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
result = response.json()

auth = (os.environ.get('USERNAME'), os.environ.get('PASSWORD'))

today_date = datetime.now().strftime('%d/%m/%Y')
now_time = datetime.now().strftime('%X')

for exercise_data in result['exercises']:
    exercise_modality = exercise_data['name']
    exercise_duration = exercise_data['duration_min']
    exercise_calories = exercise_data['nf_calories']

    row_params = {
        'workout': {
            'date': today_date,
            'time': now_time,
            'exercise': exercise_modality.title(),
            'duration': exercise_duration,
            'calories': exercise_calories
        }
    }

    requests.post(url=os.environ.get('SHEET_ENDPOINT'), json=row_params, auth=auth)