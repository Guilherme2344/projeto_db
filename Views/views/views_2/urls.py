from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_db, name='view_db'),
]