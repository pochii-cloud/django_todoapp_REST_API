"""djangoProject4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib.auth import views
from django.urls import path, include

import core
from core.views import home, delete, crossoff, uncross, getlist, deletelist, Postlist

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('delete/<int:list_id>', delete, name="delete"),
    path('crossoff/<int:list_id>', crossoff, name="crossoff"),
    path('uncross/<int:list_id>', uncross, name="uncross"),
    path('getlist/', getlist, name="getlist"),
    path('deletelist/<int:pk>/', deletelist, name="deletelist"),
    path('Postlist/', Postlist, name="Postlist"),
    path('GETLIST/', core.views.GETLIST.as_view()),
    path('DELETEVIEW/<int:List_id>/', core.views.DELETEVIEW.as_view()),
    path('postview/', core.views. postview.as_view())

]
