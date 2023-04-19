from django.db import models

class User(models.Model):
        name = models.CharField(max_length=250, null=False, default="unknown")
        email = models.EmailField(null=True)
