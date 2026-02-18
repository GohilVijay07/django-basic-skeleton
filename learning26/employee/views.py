from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm, CourseForm, DepartmentForm, ResidentPostForm


def employeeList(request):
    """Display list of employees with sorting capability"""
    sort = request.GET.get('sort', 'id')
    direction = request.GET.get('dir', 'asc')
    allowed = ['id', 'name', 'age', 'salary', 'join_date', 'post']
    if sort not in allowed:
        sort = 'id'
    order = sort if direction == 'asc' else f"-{sort}"
    employees = Employee.objects.order_by(order).values()
    return render(request, 'employee/employeeList.html', {
        "employees": employees,
        'sort': sort,
        'dir': direction
    })


def employeeFilter(request):
    """Filter employees by age >= 25"""
    employees = Employee.objects.filter(age__gte=25).values()
    return render(request, "employee/employeeList.html", {"employees": employees})


def createEmployeeWithForm(request):
    """Create a new employee"""
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("employeeList")
    else:
        form = EmployeeForm()
    return render(request, 'employee/createEmployeeForm.html', {"form": form})


def createCourseWithForm(request):
    """Create a new course"""
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("employeeList")
    else:
        form = CourseForm()
    return render(request, 'employee/createCourseWithForm.html', {"form": form})


def createDepartmentWithForm(request):
    """Create a new department"""
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("employeeList")
    else:
        form = DepartmentForm()
    return render(request, 'employee/createDepartmentWithForm.html', {"form": form})


def createresidentPostWithForm(request):
    """Create a new resident post"""
    if request.method == "POST":
        form = ResidentPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("employeeList")
    else:
        form = ResidentPostForm()
    return render(request, 'employee/createResidentPostWithForm.html', {"form": form})


def deleteEmployee(request, id):
    """Delete an employee"""
    Employee.objects.filter(id=id).delete()
    return redirect("employeeList")


def updateEmployee(request, id):
    """Update an existing employee"""
    employee = Employee.objects.get(id=id)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect("employeeList")
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employee/updateEmployeeForm.html', {"form": form})

