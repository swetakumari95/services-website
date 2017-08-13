from django.shortcuts import render
from .models import ServicesList, Services

# Create your views here.
def service_list(request):
    servicesList = ServicesList.objects.all()
    return render(request, 'servicesDisplay/service_list.html', {'servicesList': servicesList})
