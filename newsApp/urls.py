from django.contrib import admin
from django.urls import path, include

from django.conf.urls import url
from . import views   #from local directory

urlpatterns = [
    path('',views.index),
    path('readmore',views.readmore, name = "readmore"),
    path('save',views.save, name = "save"),
    path('delete',views.delete, name = "delete"),
]


# from django.conf.urls import url

# urlpatterns = [
#     url('', views.homepageview, name='home')
# ]