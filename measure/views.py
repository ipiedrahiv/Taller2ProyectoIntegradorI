from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
import requests

def measure(request):
    if request.method == "POST":
        args = {
            'type' : 'mayo26',
            'codigo' : request.POST['codigo'],
            'value' : request.POST['value'],
            'scale' : request.POST['scale'],
            'latitud' : request.POST['latitud'],
            'longitud' : request.POST['longitud'],
            'area' : request.POST['area'],
            'terreno' : request.POST['terreno'],
        }
        print(args)
        response = requests.post('https://p1-back.azurewebsites.net/', args)
        measure_json = response.json()

    response = requests.get('https://p1-back.azurewebsites.net/')
    measures = response.json()
    return render(request, "measure/measure.html", {'measures': measures})
