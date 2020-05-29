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
    path('back', views.back),

    path('all', views.view_all),
    path('all_user_uploads', views.all_uploads),
    path('all_my_uploads', views.my_uploads),
    path('my_collection', views.all_mine),
    


]
