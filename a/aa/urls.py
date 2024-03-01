from django.urls import path
from aa import views


urlpatterns = [
    path('', views.home),
]