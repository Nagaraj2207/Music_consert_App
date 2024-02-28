"""
URL configuration for music_consert_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from .import views

urlpatterns = [
    path("",views.home, name="home"),
    path("music_consert/", views.music_consert, name="music_consert"),
    path("user_logout/", views.user_logout, name="user_logout"),
    path("register", views.register, name="register"),
    path("user_login/", views.user_login, name="user_login"),
    path("book_tickets/<int:id>/", views.book_tickets, name="book_tickets"),
]