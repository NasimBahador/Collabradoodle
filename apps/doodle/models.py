from __future__ import unicode_literals
from django.db import models
from django.core.exceptions import ObjectDoesNotExist
import bcrypt, re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def validate_reg(self, request):
        errors = self.validate_inputs(request)

        if errors:
            return (False, errors)

        pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())

        user = self.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], pw_hash=pw_hash)

        return (True, user)

    def validate_login(self, request):
        try:
            user = User.objects.get(email=request.POST['email'])
            password = request.POST['password'].encode()
            if bcrypt.hashpw(password, user.pw_hash.encode()):
                return (True, user)

        except ObjectDoesNotExist:
            pass

        return (False, ["Invalid login."])

    def validate_inputs(self, request):
        errors = []

        if not request.POST['first_name']:
            errors.append('First name cannot be blank.')
        if not EMAIL_REGEX.match(request.POST['email']):
            errors.append('Invalid email.')
        if request.POST['password'] < 8:
            errors.append('Password must be at least 8 characters.')
        if request.POST['password'] != request.POST['confirm']:
            errors.append('Password and password confirm must match.')

        return errors

class DoodleManager(models.Manager):
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

    objects = UserManager()

class Doodle(models.Model):
    content = models.CharField(max_length = 300)
    doodle_creator = models.ForeignKey(User, related_name = 'user_doodle')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = DoodleManager()
