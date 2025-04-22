import requests
import pandas as pd 

request_url = "https://api.videreproject.com/metagame?format=Pauper&min_date=2025-03-22&max_date=2025-04-22&limit=32"
response = requests.get(request_url)
if response.status_code == 200:
    data = response.json()
    pd.DataFrame(data["data"]).to_csv("metagame.csv", index=False)
    print("Data retrieved successfully.")
else:   
    print(f"Failed to retrieve data. Status code: {response.status_code}")
