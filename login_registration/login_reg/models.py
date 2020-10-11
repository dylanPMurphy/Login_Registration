from django.db import models
from __future__ import unicode_literals
# Create your models here.\
class UserManager(models.Manager):
    def create_validator(self, reqPost):   
        errors = {}
        if len(reqPost['user_name'])
        return errors

class User(models.Model):
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=50)
    password = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
