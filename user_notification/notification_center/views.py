import logging

from django.http import HttpResponse
from rest_framework.decorators import api_view

from notification_center.notification_service import NotificationService


@api_view(['POST'])
def send_line_notification(request, from_system='schedule_condo_notification'):
    line_notification = NotificationService()
    try:
        line_user_id = request.data.get('line_user_id')
        messages = request.data.get('messages')
        line_notification.notify_line_template(line_user_id, messages, from_system)
        return HttpResponse('success')
    except Exception as e:
        logging.error(e)
        return HttpResponse('failed', status=500)
