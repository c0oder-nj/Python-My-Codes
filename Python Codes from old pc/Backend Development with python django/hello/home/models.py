from pyexpat import model
from django.db import models

# makemigrations - create changes and store it in a file
# Apply the pending changes created by makemigrations

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    date = models.DateField()

    def __str__(self) -> str:
        return self.name