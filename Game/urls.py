from django.urls import path
from Game import views

urlpatterns = [
    path('',views.main,name = 'main')
]