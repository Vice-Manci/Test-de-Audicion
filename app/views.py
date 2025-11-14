from django.shortcuts import render
from django.http import HttpResponse

import csv

from .models import Medition

# Create your views here.
def index(request):
    return render(request, "index/index.html")

# API & Form Views
def form(request):
    if request.method == "POST":
        print(request.POST)
        age = request.POST["age"]
        sex = request.POST.get("sex")
        audifonos = request.POST.get("audifonos")
        volume = request.POST["volume"]
        max_frecuency = request.POST["max_frequency"]

        if request.POST.get("noise") == "True":
            noise_cancelation = True
        else:
            noise_cancelation = False

        medition = Medition.objects.create(
            age=age, sex=sex, horas_audifonos=audifonos, volume=volume, noise_cancelation=noise_cancelation, noise_value=max_frecuency 
        )

        return HttpResponse(medition.noise_value)
    
def export_csv(request):
    response = HttpResponse(
        content_type="text/csv",
        headers={"Content-Disposition": 'attachment; filename="mediciones.csv"', "Content-Language": 'es-MX'}
    )
    meditions = Medition.objects.all()

    writer = csv.writer(response, dialect="excel")
    writer.writerow(
        ['Edad', 'Sexo', 'N° de horas con audífonos', 'Volumen Normal', 'Cancelación de ruido?', 'Valor hz']
    )
    for medition in meditions:
        writer.writerow([value for value in medition.__repr__()])
    
    return response