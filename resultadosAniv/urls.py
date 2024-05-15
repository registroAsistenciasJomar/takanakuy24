"""
URL configuration for resultadosAniv project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from gestorResultados import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('baile/', views.ingresar_baile),
    path('canto/', views.ingresar_canto),
    path('play_back/', views.ingresar_playback),
    path('envio_exitoso/', views.envio_exitoso),
    path('buscar_puntaje/', views.buscar_puntaje),
    path('mostrar_puntaje/', views.mostrar_puntaje),
    path('', views.inicio)
]
