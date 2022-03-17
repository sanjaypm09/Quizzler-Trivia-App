import requests

params = {
    "amount": 10,
    "type": "boolean"
}

response = requests.get("https://opentdb.com/api.php?amount=10&category=18&difficulty=medium&type=boolean",
                        params=params)
response.raise_for_status()

question_data = response.json()
question_data = question_data["results"]
