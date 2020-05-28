from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),

    path('login', views.login),
    path('register', views.register),
    
    path('dashboard', views.dashboard),
    path('success', views.success),
    path('edit', views.edit),
    path('edit_process', views.edit_process),
    path('post', views.post),
    
    path('logout', views.logout),

    path('all', views.all_mine),
    path('all_user_uploads', views.all_uploads)


]
