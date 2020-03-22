from django.shortcuts import render
from project_first_app.models import Owner
from django.http import Http404


# Create your views here.
def get_owner_info(request, owner_id):
    try:
        owner = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")

    return render(request, 'owner.html', {'owner': owner})
