from django.db import models


# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    is_superuser = models.BooleanField(default=False)

    def __str__(self):
        return self.username
