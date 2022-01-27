"""crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from .views import create_view,list_view,create_view_curso,delete_view_estudiante,delete_view_curso,update_view_estudiante,update_view_curso
urlpatterns = [
    path('admin/', admin.site.urls),
    path('estudiante/', create_view,name = 'estudiante'),
    path('curso/', create_view_curso,name = 'curso'),
    path('lista/', list_view,name = 'lista'),
    path('delete_estudiante/<int:int>', delete_view_estudiante,name = 'delete_view_estudiante' ),
    path('delete_curso/<int:int>', delete_view_curso,name = 'delete_view_curso' ),
    path('update_estudiante/<int:int>', update_view_estudiante,name = 'update_view_estudiante' ),
    path('update_curso/<int:int>', update_view_curso,name = 'update_view_curso' )
]
