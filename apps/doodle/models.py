from __future__ import unicode_literals
from django.db import models
from django.core.exceptions import ObjectDoesNotExist
import bcrypt, re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.
class UserManager(models.Manager):
    def validate_reg(self, request):
        pass
    def validate_login(self, request):
        pass
    def validate_inputs(self, request):
        pass

class DoodleManager(object):
    def post_doodle(self, request):
        pass
    def destroy_doodle(self, request):
        pass


class User(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Doodle(models.Model):
    content = models.CharField(max_length = 300)
    doodle_creator = models.ForeignKey(User, related_name = 'user_doodle')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
