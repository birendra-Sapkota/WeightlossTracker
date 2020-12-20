from django.urls import path
from . import views
from .views import register, login, logout

app_name = 'account'
urlpatterns = [
    path('register', register, name='register'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
]
