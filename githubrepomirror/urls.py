from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views 
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login, name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path("", views.home, name='home'),
    path("load/repositorios", views.load_repositorios, name='load_repositorios' ),
    path("get/repositorios", views.get_repositorios, name='get_repositorios'),
    path("all/repositorios", views.allRepos, name='allRepos'),
    path("load/organizations", views.load_organizations, name='load_organizations' ),
    path("get/organizations", views.get_organizations, name='get_organizations'),
    path("all/organizations", views.allOrganizations, name='allOrgs'),
    path("get/org/<int:org_id>", views.getOrganizationRepos, name='fetch_org'),
    path("fetch/org/<int:org_id>", views.fetchOrganizationRepos, name='fetch_org'),
    path("get/csv", views.getCSV, name='get_csv')
]