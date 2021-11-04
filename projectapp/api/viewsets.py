from rest_framework.viewsets import ModelViewSet
from .serializers import PersonSerializer, PersonSexoSerializer
from projectapp.models import Person


class PersonViewSet(ModelViewSet):
    serializer_class = PersonSerializer

    def get_queryset(self):
        return Person.objects.all().filter(cidade='Meeren', sexo='F')


class PersonSexoViewSet(ModelViewSet):
    serializer_class = PersonSexoSerializer

    def get_queryset(self):
        query_params = self.request.query_params
        sexo = query_params.get('sexo', None)
        if sexo is not None:
            return Person.objects.all().order_by('-nascimento').filter(sexo=sexo.upper())
        return Person.objects.all().order_by('-nascimento')
