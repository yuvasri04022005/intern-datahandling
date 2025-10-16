import requests
import pandas as pd

# Fetch data from a public API
url = "https://randomuser.me/api/?results=5"
response = requests.get(url)
data = response.json()

# Normalize JSON to DataFrame
users = pd.json_normalize(data['results'])
print(users[['name.first', 'email', 'location.country']])