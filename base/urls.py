from django.urls import path
from . import views

urlpatterns =[
    path('', views.index),
    path('send', views.send),
    path('add', views.add),
    path('remove', views.remove),
]