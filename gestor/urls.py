"""
URL configuration for gestor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from biblioteca import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('crearAutor/',views.crearAutor, name='crearAutor'),
    path('editarAutor/<int:autor_id>',views.editarAutor, name='editarAutor'),
    path('eliminarAutor/<int:autor_id>', views.eliminarAutor, name='eliminarAutor'),

    path('crearLibros/', views.crearLibros, name='crearLibros'),
    path('', views.listarLibros, name='listarLibros'),
    path('editarLibros/<int:libro_id>', views.editarLibro, name='editarLibros'),
    path('eliminarLibros/<int:libro_id>', views.eliminarLibro, name='eliminarLibros'),
    path('listarAutores/',views.listarAutores,name='listarAutores')
    
]
