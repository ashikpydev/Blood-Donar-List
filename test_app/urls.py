from django.urls import path
from .views import *

urlpatterns = [
    path('', user_login, name='login'),
    path('register', register, name = 'register'),
    path('all-member', all_member, name = 'all-member'),
    path('user-logout', user_logout, name = 'user-logout')


]