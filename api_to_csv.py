import requests
import pandas as pd

url = "https://didactic-disco-jj9vgv695wjg25wq-8000.app.github.dev/events"


response = requests.get(url)

if response.status_code == 200 and response.text.strip():
    try:
        data = response.json()
        df = pd.DataFrame(data)
        df.to_csv("events_data.csv", index=False)
        df.to_excel("events_data.xlsx", index=False)
        print("Data saved to CSV and Excel.")
    except Exception as e:
        print("Failed to parse JSON or save file:", e)
else:
    print("Empty or invalid response received from API.")
