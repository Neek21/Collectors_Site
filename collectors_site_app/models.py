from django.db import models
import re

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        email_check = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        logged_email = User.objects.filter(email=postData['email'])

        if not email_check.match(postData['email']):
            errors['email'] = "Invalid email address!"
        if len(logged_email) > 0:
            errors['email_in_use'] = "Email is already in use"
        if len(postData['password']) < 8:
            errors['password'] = "Your password must be at least 8 characters."
        if postData['password'] != postData['confirm_pass']:
            errors['confirm_password'] = "Password and Confirm password must match."
        if len(postData['first_name']) <4 or len(postData['last_name']) <4: 
            errors['first_last_name'] = "First and last name must be at least 4 characers."

        return errors

    def edit_validator(self, postData):
        errors = {}
        email_check = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        
        if not email_check.match(postData['email']):
            errors['email'] = "Invalid email address!"
        if len(postData['new_password']) < 8:
            errors['password'] = "Your password must be at least 8 characters."
        if postData['new_password'] != postData['confirm_pass']:
            errors['confirm_password'] = "New password and confirm password must match."
        if len(postData['first_name']) <4 or len(postData['last_name']) <4: 
            errors['first_last_name'] = "First and last name must be at least 4 characers."

        return errors

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Post(models.Model):
    post_image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=50)
    poster = models.ForeignKey(User, related_name='posts', on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)