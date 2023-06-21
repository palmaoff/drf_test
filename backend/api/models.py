from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Transaction(models.Model):
    value = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.id}"
    

class Balance(models.Model):
    score = models.IntegerField(default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}"
