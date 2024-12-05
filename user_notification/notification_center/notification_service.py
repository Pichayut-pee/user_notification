import json
import logging

from dotenv import load_dotenv
import os
import requests

from user_notification.util.exception import ServerErrorException


class NotificationService:

    def __init__(self):
        load_dotenv()
        self.line_message_api = os.getenv("LINE_MESSAGE_API")
        self.line_token = os.getenv("LINE_MESSAGE_TOKEN")

    def notify_line_template(self, line_user_id, messages):
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'Bearer ' + self.line_token
                   }

        for i in range(0, len(messages), 5):
            image_urls, titles, texts, links = [], [], [], []
            for msg in messages[i:i + 5]:
                image_urls.append(msg['image_url'])
                tmp_title = str(msg['title'])
                if len(tmp_title) > 35:
                    tmp_title = tmp_title[:35] + '...'

                tmp_text = str(msg['text'])
                if len(tmp_text) > 50:
                    tmp_text = tmp_text[:50] + '...'

                titles.append(tmp_title)
                texts.append(tmp_text)
                links.append(msg['link'])

            request_messages = [{"type": "template",
                                 "altText": "Condo Alert",
                                 "template": {
                                     "type": "buttons",
                                     "thumbnailImageUrl": str(image_url),
                                     "imageAspectRatio": "rectangle",
                                     "imageSize": "cover",
                                     "imageBackgroundColor": "#FFFFFF",
                                     "title": str(title),
                                     "text": str(text),
                                     "defaultAction": {
                                         "type": "uri",
                                         "label": "View detail",
                                         "uri": str(link)
                                     },
                                     "actions": [
                                         {
                                             "type": "uri",
                                             "label": "View detail",
                                             "uri": str(link)
                                         }
                                     ]
                                 }
                                 } for image_url, title, text, link in zip(image_urls, titles, texts, links)]

            data = {
                "to": str(line_user_id),

                "messages": request_messages

            }
            try:
                response = requests.post(self.line_message_api, headers=headers, json=data)
                if response.status_code != 200:
                    logging.error(response.text)
                    raise Exception('Failed to send message to LINE')
            except Exception as e:
                logging.error(e + ' ' + str(request_messages))
                raise ServerErrorException('Failed to send message to LINE')
