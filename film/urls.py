from django.urls import path
from . import views

app_name = 'film'

urlpatterns = [
	path('', views.index, name='index'),
	path('post/<slugInput>/', views.detailPost, name='detail'),
]