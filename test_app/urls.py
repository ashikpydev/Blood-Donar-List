from django.urls import path
from .views import *

urlpatterns = [
    path('', user_login, name='login'),
    path('register', register, name = 'register'),
    path('all-member', all_member, name = 'all-member'),
    path('user-logout', user_logout, name = 'user-logout'),
    path('user-profile/<int:id>', user_profile, name = 'user_profile'),
    path("my-profile", my_profile, name="my_profile"),
    path('upload/', upload_image, name = 'upload')


]