from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),

    path('login', views.login),
    path('register', views.register),
    path('edit_profile', views.edit_profile),
    
    path('dashboard', views.dashboard),
    path('success', views.success),
    path('edit', views.edit),
    
    path('logout', views.logout),

]