from __future__ import unicode_literals
from django.db import models


class UserManager(models.Manager):
    def reg_validation(self, postData):
        errors = {}
        if len(postData['username']) < 5:
            errors['username'] = "Username must be at least 5 characters"
        if len(postData['email']) < 1:
            errors['email'] = "Email must be valid"
        return errors
    
    def login_validation(self, postData):
        errors = {}
        return errors


class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    objects = UserManager()