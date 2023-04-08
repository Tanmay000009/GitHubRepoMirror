"Pipelines for social auth"
from core.models import UserProfile

from .models import User

def create_user_profile(backend, user, response, *args, **kwargs):
    "Create user profile with avatar url and uid"
    profile = UserProfile.objects.filter(user=user).first()
    if not profile:
        profile = UserProfile(user=user)
    if 'avatar_url' in response:
        profile.avatar_url = response['avatar_url']
    if 'id' in response:
        profile.uid = response['id']
    if 'access_token' in response:
        profile.access_token = response['access_token']
    if 'html_url' in response:
        profile.url = response['html_url']
    profile.save()

    
