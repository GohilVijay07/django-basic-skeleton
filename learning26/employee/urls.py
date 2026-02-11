
from . import views
from django.urls import path
urlpatterns = [
    path('employeeList/', views.employeeList),
    path('employeeFilter/', views.employeeFilter),
    path('createEmployeeWithForm/', views.createEmployeeWithForm),
    path('createCourseWithForm/', views.createCourseWithForm),
    path('createDepartmentWithForm/', views.createDepartmentWithForm),
    path('createResidentPostWithForm/', views.createresidentPostWithForm),
]