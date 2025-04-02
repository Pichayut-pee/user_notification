import requests
import os
from user_notification.util.alert import send_alert

tiny_url_api = os.getenv("TINY_URL_API")
tiny_url_token = os.getenv("TINY_URL_TOKEN")

headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer ' + tiny_url_token
           }


def shorten_url(long_url, unique_id):
    data = {
        "url": long_url,
        "domain": "hobinnovations.live",
        "alias": str(unique_id),
        "tags": "condo,link",
        "description": "string"
    }
    try:
        response = requests.post(tiny_url_api+'/create', headers=headers, json=data)
    except Exception as e:
        send_alert("Failed to send message to LINE: " + str(e))
        print("Error from tiny url" + str(e))
        return None

    return response.json()['data']['tiny_url']
