from django.urls import path
from . import views #(to call the views.py file from the same directory)

urlpatterns = [
    # path for the say_hello view
	path('hello/', views.say_hello),
    # path for the home page of the stockregit app
    path('', views.home)
]