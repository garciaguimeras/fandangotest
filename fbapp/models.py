from django.db import models

class FacebookUser(models.Model):
    facebook_id = models.CharField(max_length=64)
    name = models.CharField(max_length=200)

