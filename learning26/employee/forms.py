from django import forms
from .models import Employee, Course, department, ResidentPost

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = department
        fields = "__all__"

class ResidentPostForm(forms.ModelForm):
    class Meta:
        model = ResidentPost
        fields = "__all__"