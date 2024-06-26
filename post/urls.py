from django.urls import path
from post import views

app_name = 'post'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('create/', views.post_create, name='post_create'),
]
