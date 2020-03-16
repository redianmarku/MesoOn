from django.urls import path

from users.views import Profile

app_name = 'users'

urlpatterns = [
    path('profile/', Profile, name='profile'),

]
