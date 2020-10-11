from django.db import models
from __future__ import unicode_literals
# Create your models here.\
class UserManager(models.Manager):
    def create_validator(self, reqPost):   
        errors = {}
        if len(reqPost['user_name'])<5:
            errors['username'] = "Name must be at least 5 characters"
        if len(reqPost['email'])<8:
            errors['email'] = "Email must be at least 8 characters"
        if len(reqPost['password'])<8:
            errors['password'] = "Password must be at least 8 characters"
        return errors

class User(models.Model):
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=50)
    password = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
