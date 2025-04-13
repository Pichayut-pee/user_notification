import requests
import json

ERROR_WEBHOOK_URL = 'https://discordapp.com/api/webhooks/1350265746243977298/ez0SddlwDqN-07cYwiP3VImUFriwjBPotN6dSaiHBPz0YLiOd57i2UpG4h7N4IAVs1Bh'
USER_MONITORING_WEBHOOK_URL = 'https://discordapp.com/api/webhooks/1360641225983787169/7-p7OxN5krx7mej4s4R8IHpR-XiV-RfBAzuqcvOpMNf1qAGmTDDP_UDNNLG4p5qkLbB9'


def send_alert(message: str):
    # Construct the payload
    payload = {
        "content": message
    }

    headers = {
        "Content-Type": "application/json"
    }

    # Send POST request to Discord Webhook URL
    response = requests.post(ERROR_WEBHOOK_URL, data=json.dumps(payload), headers=headers)

    # Check if the request was successful
    if response.status_code == 204:
        print("Alert sent successfully!")
    else:
        print(f"Failed to send alert: {response.status_code} - {response.text}")


def send_user_monitoring(message: str):
    payload = {
        "content": message
    }

    headers = {
        "Content-Type": "application/json"
    }

    # Send POST request to Discord Webhook URL
    response = requests.post(USER_MONITORING_WEBHOOK_URL, data=json.dumps(payload), headers=headers)

    # Check if the request was successful
    if response.status_code == 204:
        print("User monitoring sent successfully!")
    else:
        print(f"Failed to send user monitoring: {response.status_code} - {response.text}")
