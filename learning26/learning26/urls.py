"""
URL configuration for learning26 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.contrib import admin# type: ignore
from django.urls import path# type: ignore
from . import views
from django.urls import include# type: ignore
#from views import test

#localhost:8000/test/
urlpatterns = [
    path('admin/', admin.site.urls),
    
    path("test/",views.test),
    path("about/",views.AboutUs),
    path("contact/",views.contactUs),
    path("",views.home),
    #http://127.0.0.1/:8000/recap
    path("recap/",views.reacp),
    path("recipe/",views.recipe),

    #app level url config
    path("student/",include("student.urls")),
    path("student2/",include("student2.urls")),
    path("employee/",include("employee.urls"))
    

]
