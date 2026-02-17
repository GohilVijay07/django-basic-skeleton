from django.urls import path
from . import views

urlpatterns = [
    path('serviceList/', views.serviceList, name='serviceList'),
    path('createServiceWithForm/', views.createServiceWithForm, name='createServiceWithForm'),
    path('updateService/<int:id>/', views.updateService, name='updateService'),
    path('deleteService/<int:id>/', views.deleteService, name='deleteService'),
]
