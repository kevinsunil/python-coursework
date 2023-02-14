import requests
from datetime import datetime
APP_ID = "APP_ID"
APP_KEY = "APP_KEY"
APP_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}
user_parameters = {
    "query": input("Enter the exercise you did?"),
    "gender": "male",
    "age": 21
}
today = datetime.now()
SHEETY_URL = "https://api.sheety.co/85a34d36ef8134fe007b70545d4ada62/myWorkouts/workouts"

response = requests.post(url=APP_URL, json=user_parameters, headers=headers)
response.raise_for_status()
data = response.json()["exercises"]
sheety_headers ={
    "Authorization": "Bearer TOKEN"
}
for new_data in data:
    sheet_parameter = {
        "workout": {
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime('%X'),
            "exercise": new_data["name"].title(),
            "duration": round(new_data["duration_min"]),
            "calories": round(new_data["nf_calories"])
        }
    }
    new_exercise = requests.post(url=SHEETY_URL, json=sheet_parameter, headers=sheety_headers)
    print(new_exercise.text)

