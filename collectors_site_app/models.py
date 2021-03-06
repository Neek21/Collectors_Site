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
        if len(postData['bio']) > 255:
            errors['bio'] = "Your bio can only be 255 characters long."

        return errors

class CommentManager(models.Manager):
    def comment_validator(self, postData):
        errors ={}
        if len(postData['comment']) > 255:
            errors['comment_too_long'] = "The comment can only be 255 characters"
        if len(postData['comment']) == 0:
            errors['comment_empty'] = "Write a comment"
        
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    bio = models.CharField(max_length=255, default='')
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Post(models.Model):
    post_image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=50)
    poster = models.ForeignKey(User, related_name='posts', on_delete = models.CASCADE)
    user_likes = models.ManyToManyField(User, related_name='liked_posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    comment = models.CharField(max_length=255)
    poster = models.ForeignKey(User, related_name='user_comments', on_delete = models.CASCADE)
    post_comment = models.ForeignKey(Post, related_name='post_comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CommentManager()

class Avatar(models.Model):
    upload_avatar= models.ImageField(upload_to='images/')
    avatar_description = models.CharField(max_length=50)
    avatar_loader = models.ForeignKey(User, related_name='upload_avatar', on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)