from django.contrib import admin # type: ignore
from .models import Employee, Course, department, ResidentPost
# Register your models here.
admin.site.register(Employee)
admin.site.register(Course)
admin.site.register(department)
admin.site.register(ResidentPost)