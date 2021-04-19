from django.contrib import admin
from django.urls import path, include

from django.conf.urls import url
from . import views   #from local directory

urlpatterns = [
    path('',views.index),
    path('readmore', views.readmore, name = "readmore"),
    path('save', views.save, name = "save"),
    path('delete', views.delete, name = "delete"),
    path('sports', views.sports, name = "sports"),
    path('science', views.science, name = "science"),
    path('india', views.india, name = "india"),
    path('entertainment', views.entertainment, name = "entertainment"),
    path('us', views.us, name = "us"),
    path('health', views.health, name = "health"),
    path('world', views.world, name = "world"),
]



# from django.conf.urls import url

# urlpatterns = [
#     url('', views.homepageview, name='home')
# ]