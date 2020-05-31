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
    path('back', views.back),

    path('post', views.post),
    
    path('logout', views.logout),
    path('back', views.back),

<<<<<<< HEAD
    path('all', views.view_all),
    path('all_user_uploads', views.all_uploads),
    path('all_my_uploads', views.my_uploads),
    path('my_collection', views.all_mine),
    
=======
    path('all', views.all_mine),
    path('all_user_uploads', views.all_uploads),
    path('my_collection', views.my_collection),
>>>>>>> 4ffdd2b6f42dcd91d1e21ccb9c2716b181715fb5


]
