import requests
import json

WEBHOOK_URL = 'https://discordapp.com/api/webhooks/1350265746243977298/ez0SddlwDqN-07cYwiP3VImUFriwjBPotN6dSaiHBPz0YLiOd57i2UpG4h7N4IAVs1Bh'

def send_alert(message: str):
    # Construct the payload
    payload = {
        "content": message
    }

    headers = {
        "Content-Type": "application/json"
    }

    # Send POST request to Discord Webhook URL
    response = requests.post(WEBHOOK_URL, data=json.dumps(payload), headers=headers)

    # Check if the request was successful
    if response.status_code == 204:
        print("Alert sent successfully!")
    else:
        print(f"Failed to send alert: {response.status_code} - {response.text}")
