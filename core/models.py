"Module for models"
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    "Model for user profile"
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar_url = models.URLField(blank=True, null=True)
    uid = models.CharField(max_length=255, blank=True, null=True)
    access_token = models.CharField(max_length=255, blank=True, null=True)
    url = models.URLField(blank=True, null=True)

class UserOrganizations(models.Model):
    "Model for user organizations"
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organizations')
    name = models.CharField(max_length=255)
    id = models.IntegerField(primary_key=True)
    url = models.URLField(blank=True, null=True)
    avatar_url = models.URLField(blank=True, null=True)
    

class UserRepositories(models.Model):
    "Model for user repositories"
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='repositories')
    organization = models.ManyToOneRel(UserOrganizations, related_name='repositories', to='UserOrganizations', on_delete=models.CASCADE, field_name='organization')
    name = models.CharField(max_length=255)
    id = models.IntegerField(primary_key=True)
    owner_id = models.IntegerField(blank=True, null=True)
    owner_name = models.CharField(max_length=255, blank=True, null=True)
    owner_email = models.EmailField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    stars = models.IntegerField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)