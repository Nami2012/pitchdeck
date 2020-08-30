"""pitchdeck URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from creator import views as creator_views
from creator import generate as generate_views
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',creator_views.home),
    path('home/', creator_views.home, name='home'),
    
    path('accounts/profile/', creator_views.profile, name='profile'),
    path('profile/update/', creator_views.profile_update, name='profile-update'),
    path('signup/',creator_views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='authenticate/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='authenticate/logout.html'), name='logout'),    

    #generate urls

    path('input/', creator_views.input, name='input'),
    path('input/next/<int:pk>/', generate_views.next, name='next'),



]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
