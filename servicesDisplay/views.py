from django.shortcuts import render

# Create your views here.
def service_list(request):
    return render(request, 'servicesDisplay/service_list.html', {})
