from django.shortcuts import render

# Create your views here.

from django.http import Http404
from django.shortcuts import render
from .models import Car, Owner
from django.views.generic import ListView
from .forms import AddOwnerForm
from django.views.generic.edit import CreateView
from django.urls import reverse



def owner(request, owner_id):
    try:
        p = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("Does not exist")
    return render(request, 'zimarinapp/detail.html', {'owner': p})

def cars(request):
    try:
        p = Car.objects.all()
    except Car.DoesNotExist:
        raise Http404("Does not exist")
    return render(request, 'zimarinapp/cars.html', {'cars': p})

def all_owners(request):
    try:
        p = Owner.objects.all()
    except Owner.DoesNotExist:
        raise Http404("Does not exist")
    return render(request, 'zimarinapp/owners.html', {'owners': p})


class AllCars(ListView):
    model = Car
    context_object_name = 'cars'
    template_name = 'zimarinapp/cars.html'

def add_owner(request):
    form = AddOwnerForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'zimarinapp/add_owner.html', {'add_owner': form})


class AddCar(CreateView):
    model = Car
    fields = ['brand', 'model', 'color', 'number']
    template_name = 'zimarinapp/add_car.html'
