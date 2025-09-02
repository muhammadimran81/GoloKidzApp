from django.urls import path
from . import views

urlpatterns = [
    path('function', views.hello_world),
    path('class', views.HelloPak.as_view()),
    path('reservation', views.home),

]