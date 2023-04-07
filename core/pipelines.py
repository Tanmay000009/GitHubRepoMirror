"Pipelines for social auth"
from core.models import UserProfile, UserRepositories

def create_user_profile(backend, user, response, *args, **kwargs):
    "Create user profile with avatar url and uid"
    profile = UserProfile.objects.filter(id=user.id).first()
    if not profile:
        profile = UserProfile(user=user)
    if 'avatar_url' in response:
        profile.avatar_url = response['avatar_url']
    if 'id' in response:
        profile.uid = response['id']
    profile.save()

def create_user_repositories(backend, user, response, *args, **kwargs):
    "Create user repositories"
    print(user.username)
    
