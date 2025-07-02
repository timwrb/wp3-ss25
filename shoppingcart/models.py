from django.conf import settings
from django.db import models

# Create your models here.
class Customer(models.Model):
    salutation = models.CharField(max_length=5)
    '''
    firstname = models.CharField(max_length=15)
    lastname = models.CharField(max_length=15)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    '''
    birthdate = models.DateField()

    user =models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def firstname(self):
        return self.user.firstname

    def lastname(self):
        return self.user.lastname

    def email(self):
        return self.user.email



