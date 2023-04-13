from django.urls import path, include
from . import views

app_name = 'reviews'
urlpatterns = [
    path('', views.index, name='index'),

]