from django.db import models
from datetime import datetime

class Contact(models.Model):
    date = models.DateTimeField(default=datetime.now, blank=True)
    text = models.TextField()
    email = models.CharField(max_length=120)
