import requests

parametrs = {
    "amount": 10, 
    "difficulty": "easy",
    "type": "boolean"
}

response = requests.get(url="https://opentdb.com/api.php", params=parametrs)
response.raise_for_status
data = response.json()['results']


question_data = data



