from django.contrib import admin
from .models import UserProfile, UserRepositories, UserOrganizations

admin.site.register(UserProfile)
admin.site.register(UserRepositories)
admin.site.register(UserOrganizations)