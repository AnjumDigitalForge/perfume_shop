from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# This file contains the view functions that handle the logic for the stockregit app.

# say_hello view is a test view.
def say_hello(request):
	return HttpResponse("<h1>Hello World</h1>")

# home view is the main view for the stockregit app.
def home(request):
    return HttpResponse("""
        <h1>Welcome to My Django Project!</h1>
        <p>Development server is running correctly.</p>
        <ul>
            <li><a href="/admin/">Admin Panel</a></li>
            <li><a href="/stockregit/">Stockregit App</a></li>
        </ul>
        <p>You can now build your Django project!</p>
    """)