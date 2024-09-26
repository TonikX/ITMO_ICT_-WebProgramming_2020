from django.http import Http404
from django.shortcuts import render
from rpd.models import CarOwner

def detail(request, CarOwner):
    try:
        car_owner = CarOwner.objects.get(pk=CarOwner_id)
    except CarOwner.DoesNotExist:
        raise Http404("CarOwner does not exist")
    return render(request, 'rpd/detail.html', {'CarOwner First name': car_owner})