from django.shortcuts import render, redirect
from .models import Service
from .forms import ServiceForm


def serviceList(request):
    services = Service.objects.order_by('id').values()
    return render(request, 'services/serviceList.html', {"services": services})


def createServiceWithForm(request):
    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("serviceList")
    else:
        form = ServiceForm()
    return render(request, 'services/createServiceForm.html', {"form": form})


def updateService(request, id):
    service = Service.objects.get(id=id)
    if request.method == "POST":
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect("serviceList")
    else:
        form = ServiceForm(instance=service)
    return render(request, 'services/updateServiceForm.html', {"form": form})


def deleteService(request, id):
    Service.objects.filter(id=id).delete()
    return redirect("serviceList")
