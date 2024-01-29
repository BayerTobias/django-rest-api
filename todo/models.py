from django.db import models
import datetime
from datetime import date
from django.contrib.auth.models import User


class Todo(models.Model):
    title = models.CharField(max_length=30, null=True, blank=True)
    description = models.CharField(max_length=30, null=True, blank=True)
    created_at = models.DateField(default=datetime.date.today())
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    def time_passed(self):
        today = date.today()
        delta = today - self.created_at

        return delta.days
