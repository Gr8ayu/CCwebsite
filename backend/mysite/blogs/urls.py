from django.urls import path,include, re_path
from . import views







urlpatterns = [
    

    path('', views.getPosts.as_view()),
    path('add/', views.addPost.as_view()),
    path('edit/<int:id>', views.editPost.as_view()),
    path('<int:id>/', views.getPost.as_view()),
    path('projects', views.getProjects.as_view()),
    
]