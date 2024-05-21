from django.db import models

# Create your models here.
class Message(models.Model):
    message=models.CharField(max_length=255)
    sender=models.CharField(max_length=30)
    reciver=models.CharField(max_length=30)




