from django.urls import path

from users.views import Profile, kerkesa

app_name = 'users'

urlpatterns = [
    path('profile/', Profile, name='profile'),
    path('kerkesa/', kerkesa, name='kerkesa')

]
