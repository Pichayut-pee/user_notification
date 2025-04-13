from django.db import models
from django.utils import timezone

import django
from django.db import models


# Create your models here.
class NotificationLog(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.TextField()
    message = models.JSONField()
    created_at = models.DateTimeField(default=django.utils.timezone.now)
    from_system = models.TextField(default="schedule_condo_notification")

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "message": self.message,
            "created_at": self.created_at
        }
