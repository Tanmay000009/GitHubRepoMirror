from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.core.exceptions import ObjectDoesNotExist
from .models import UserRepositories, UserOrganizations
import requests
import json
# Create your views here.


def login(request):
    return render(request, 'login.html')

@login_required
def home(request):
    repos = UserRepositories.objects.filter(user=request.user.id)[:5]
    orgs = UserOrganizations.objects.filter(user=request.user.id)[:5]
    return render(request, 'home.html', {'repos': repos, 'orgs': orgs})

@login_required
def allRepos(request):
    repos = UserRepositories.objects.filter(user=request.user.id)
    return render(request, 'allRepos.html', {'repos': repos})

@login_required
def load_repositorios(request):
    return render(request, 'loadRepo.html')

@login_required
def get_repositorios(request):
    access_token = request.user.userprofile.access_token

    headers = {
        'Authorization': f'token {access_token}',
        'Accept': 'application/vnd.github.v3+json'
    }

    page_num = 1
    repos = []
    failure = False
    unauthorized = False

    while True:
        response = requests.get(f'https://api.github.com/user/repos?per_page=30&page={page_num}', headers=headers)

        if response.status_code == 401:
            logout(request)
            unauthorized = True
            break

        if response.status_code != 200:
            response = requests.get(f'https://api.github.com/user/repos?per_page=30&page={page_num}', headers=headers)
            
            if response.status_code == 401:
                logout(request)
                unauthorized = True
                break
            
            if response.status_code != 200:
                failure = True
                break


        repos_page = json.loads(response.text)
        repos.extend(repos_page)

        if len(repos_page) == 0:
            break

        page_num += 1

    if unauthorized:
        return JsonResponse({"status": "unauthorized"})
    
    if failure:
        return JsonResponse({"status": "failure"})

    filteredData = [{
        "id": repo["id"],
        "name": repo["name"],
        "owner_id": repo["owner"]["id"],
        "owner_name": repo["owner"]["login"],
        "owner_email": repo["owner"]["email"] if "email" in repo["owner"] else None,   
        "status": "private" if repo["private"] else "public",
        "stars": repo["stargazers_count"],
        "url": repo["html_url"]
    } for repo in repos]
        
    # save or update repositories
    for repo in filteredData:
        try:
            user_repo = UserRepositories.objects.get(id=repo['id'])
            user_repo.name = repo['name']
            user_repo.owner_id = repo['owner_id']
            user_repo.owner_name = repo['owner_name']
            user_repo.owner_email = repo['owner_email']
            user_repo.status = repo['status']
            user_repo.stars = repo['stars']
            user_repo.url = repo['url']
            user_repo.save()
        except ObjectDoesNotExist:
            user_repo = UserRepositories.objects.create(
                user=request.user,  
                name=repo['name'],
                id=repo['id'],
                owner_id=repo['owner_id'],
                owner_name=repo['owner_name'],
                owner_email=repo['owner_email'],
                status=repo['status'],
                stars=repo['stars'],
                url=repo['url']
            )
            user_repo.save()


    return JsonResponse({"status": "success"})

@login_required
def load_organizations(request):
    return render(request, 'loadOrg.html')

@login_required
def get_organizations(request):
    
    access_token = request.user.userprofile.access_token

    headers = {
        'Authorization': f'token {access_token}',
        'Accept': 'application/vnd.github.v3+json'
    }

    page_num = 1
    orgs = []
    failure = False
    unauthorized = False

    while True:
        response = requests.get(f'https://api.github.com/user/orgs?per_page=30&page={page_num}', headers=headers)
        if response.status_code == 401:
            logout(request)
            unauthorized = True
            break

        if response.status_code != 200:
            response = requests.get(f'https://api.github.com/user/orgs?per_page=30&page={page_num}', headers=headers)
            
            if response.status_code == 401:
                logout(request)
                unauthorized = True
                break
            
            if response.status_code != 200:
                failure = True
                break

        orgs_page = json.loads(response.text)
        orgs.extend(orgs_page)

        if len(orgs_page) == 0:
            break

        page_num += 1
    
    if unauthorized:
        return JsonResponse({"status": "unauthorized"})
    
    if failure:
        return JsonResponse({"status": "failure"})
    
    print(orgs)

    filteredData = [{
        "id": org["id"],
        "name": org["login"],
        "url": org["url"]
    } for org in orgs]

    # save or update organizations
    for org in filteredData:
        try:
            user_org = UserOrganizations.objects.get(id=org['id'])
            user_org.name = org['name']
            user_org.url = org['url']
            user_org.save()
        except ObjectDoesNotExist:
            user_org = UserOrganizations.objects.create(
                user=request.user,  
                name=org['name'],
                id=org['id'],
                url=org['url']
            )
    
    return JsonResponse({"status": "success"})