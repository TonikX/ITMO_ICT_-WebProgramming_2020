import datetime
from django.http import Http404 
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from project_first_app.models import Ownership, Car, Owner
from project_first_app.forms import OwnerForm


class ListCars(ListView):
    model = Car


class CreateCars(CreateView):
    model = Car
    fields = ['model', 'brand', 'color', 'car_number']
    success_url = '/create_car/'


def get_owner(request, c_id):
    try:
        now = datetime.datetime.now()
        date = str(now.year) + '-' + str(now.month) + '-' + str(now.day)
        ownership = Ownership.objects.filter(car_id=c_id).filter(date_of_start__lte=date).filter(date_of_end__gte=date)[0]
        owner = Owner.objects.get(id=ownership.owner_id)
    except Car.DoesNotExist:
        raise Http404("Does not exist")
    return render(request, 'owner.html', {'owner': owner})


def list_owners(request):
    context = {}
    context['owners'] = Owner.objects.all()
    return render(request, 'owners_list.html', context)


def create_owner(request):
    context = {}
    form = OwnerForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, 'create_owner.html', context)
