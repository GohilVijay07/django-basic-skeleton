from . import views
from django.urls import path # type: ignore

urlpatterns = [
    path('employeeList/', views.employeeList, name='employeeList'),
    path('createEmployeeWithForm/', views.createEmployeeWithForm, name='createEmployeeWithForm'),
    path('createCourseWithForm/', views.createCourseWithForm),
    path('createDepartmentWithForm/', views.createDepartmentWithForm, name='createDepartmentWithForm'),
    path('createResidentPostWithForm/', views.createresidentPostWithForm, name='createresidentPostWithForm'),
    path('deleteEmployee/<int:id>/', views.deleteEmployee, name='deleteEmployee'),
    path('filterEmployee/', views.employeeFilter, name='filterEmployee'),
    path('updateEmployee/<int:id>/', views.updateEmployee, name='updateEmployee'),
]