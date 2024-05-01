from django.db import models

# Create your models here.
class Club(models.Model):
  name = models.CharField(max_length=255)
  description = models.CharField(max_length=255)
  sponsor_name = models.CharField(max_length=255, default="TBD")
  sponsor_email = models.CharField(max_length=255, default="TBD")
  meeting_times = models.CharField(max_length=255, default="TBD")
  location = models.CharField(max_length=255, default="TBD")
