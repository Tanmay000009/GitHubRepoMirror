from django.contrib import admin
from .models import UserProfile, UserRepositories

admin.site.register(UserProfile)
admin.site.register(UserRepositories)