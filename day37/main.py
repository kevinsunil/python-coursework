import requests
from datetime import datetime
PIXELA_URL = "https://pixe.la/v1/users"
USERNAME = "kevin7"
TOKEN = "KEY"
user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=PIXELA_URL, json=user_parameters)
# print(response.text)
NEW_GRAPH_ENDPOINT = f"{PIXELA_URL}/{USERNAME}/graphs"
headers = {
    "X-USER-TOKEN": TOKEN
}
GRAPH_ID = "graph1"
graph_parameters = {
    "id": GRAPH_ID,
    "name": "Daily reading",
    "unit": "Pages",
    "type": "int",
    "color": "ajisai",
    "timezone": "Asia/Calcutta"
}
# response = requests.post(url=NEW_GRAPH_ENDPOINT, json=graph_parameters, headers=headers)
# print(response.text)
today = datetime.now()
NEW_PIXEL_ENDPOINT = f"{NEW_GRAPH_ENDPOINT}/{GRAPH_ID}"
pixel_parameters = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many pages did you read today?"),
}

response = requests.post(url=NEW_PIXEL_ENDPOINT, json=pixel_parameters, headers=headers)
print(response.text)

UPDATE_PIXEL_ENDPOINT = f"{NEW_PIXEL_ENDPOINT}/20230211"
update_parameters = {
    "quantity": "10"
}

# response = requests.put(url=UPDATE_PIXEL_ENDPOINT, json=update_parameters, headers=headers)
# print(response.text)

# Delete pixel
# response = requests.delete(url=UPDATE_PIXEL_ENDPOINT, headers=headers)
# print(response.text)
