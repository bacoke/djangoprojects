from django.urls import path
from . import views

app_name = 'film'

urlpatterns = [
	path('', views.index, name='index'),
	path('addpost/', views.addPost, name='addpost'),
	path('post/<slugInput>/', views.detailPost, name='detail'),
	path('category/<categoryInput>/', views.categoryPost, name='category'),
]