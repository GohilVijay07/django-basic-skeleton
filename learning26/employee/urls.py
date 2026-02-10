
from . import views
from django.urls import path
urlpatterns = [
    path('employeeList/', views.employeeList),
    path('employeeFilter/', views.employeeFilter),
]