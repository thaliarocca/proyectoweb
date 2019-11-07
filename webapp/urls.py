"""webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from blog import views
from marvel import views as marvelviews
urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/', views.welcome, name='bienvenido'),
    path('entradas/', views.entradas, name='entradas'),
    path('autores/', views.autores,name='autores'),
    path('autores/<int:id>', views.edit_autor,name='edit_autor'),
    path('autores/eliminar/<int:id>', views.delete_autor,name='delete_autor'),

    path('mostrar/', marvelviews.show,name='show'),
    path('clienteget/',marvelviews.cget,name='clienteget')
]
