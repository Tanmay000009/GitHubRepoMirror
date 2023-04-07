from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import requests
# Create your views here.


def login(request):
    return render(request, 'login.html')

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def load_repositorios(request):
    return render(request, 'loadRepo.html')

@login_required
def get_repositorios(request):
    id = request.user.id
    access_token = request.user.userprofile.access_token

    url = 'https://api.github.com/user/repos'

    headers = {
        'Authorization': f'token {access_token}',
        'Accept': 'application/vnd.github.v3+json'
    }

    response = requests.get('https://api.github.com/user/repos', headers=headers)

    if response.status_code == 200:
        data = {"status": "success"}
    elif response.status_code == 401:
        logout(request)
        data = {"status": "unauthorized"}
    else:
        data = {"status": "error"}

    return JsonResponse(data)