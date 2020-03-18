"""Coursera URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import  handler404, handler403, handler500

handler404 = 'courses.views.view_404'
handler500 = 'courses.views.view_500'
handler403 = 'courses.views.view_403'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('courses.urls',namespace='courses')),
    path('', include('blog.urls',namespace='blogs')),
    path('', include('memberships.urls',namespace='memberships')),
    path('', include('users.urls',namespace='users')),
    path('accounts/', include('allauth.urls')),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
