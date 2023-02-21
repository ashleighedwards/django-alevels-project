from __future__ import unicode_literals
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    description = models.CharField(max_length=30, default='')
    email = models.EmailField(max_length=50, default=0)

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])
post_save.connect(create_profile, sender=User)

class AddItem(models.Model):
    item = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class AddTheItems(models.Model):
    item_choice = models.CharField(max_length=100, default='')
    many_items = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(1000)])
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class RemoveItem(models.Model):
    item = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class RemoveTheItems(models.Model):
    item_choice = models.CharField(max_length=100, default='')
    many_items = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(1000)])
    crime_type = models.CharField(max_length=100, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Post(models.Model):
    post = models.CharField(max_length=500, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
