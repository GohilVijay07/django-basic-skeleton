from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='society_index'),
]
