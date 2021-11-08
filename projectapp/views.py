from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse
from .resources import PersonResource
from tablib import Dataset
from .models import Person
from datetime import datetime


def export(request):
    person_resource = PersonResource()
    dataset = person_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="data.xls"'
    return response


def simple_upload(request):
    if request.method == 'POST':
        person_resource = PersonResource()
        dataset = Dataset()
        new_person = request.FILES['myfile']

        if not new_person.name.endswith('xlsx'):
            messages.info(request, 'wrong format')
            return render(request, 'projectapp/upload.html')

        imported_data = dataset.load(new_person.read(), format='xlsx')
        for data in imported_data:
            print(data[2])
            value = Person(
                    nome=data[2],
                    sobrenome=data[3],
                    sexo=data[4],
                    altura=data[5],
                    peso=data[6],
                    nascimento=datetime.utcfromtimestamp(data[7]).strftime('%Y-%m-%d'),
                    bairro=data[8],
                    cidade=data[9],
                    estado=data[10],
                    numero=data[11]
                )
            value.save()
    return render(request, 'projectapp/upload.html')
