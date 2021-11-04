from rest_framework.serializers import ModelSerializer
from projectapp.models import Person


class PersonSerializer(ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'nome', 'sobrenome',
                  'sexo', 'altura', 'peso',
                  'nascimento', 'bairro', 'cidade',
                  'estado', 'numero')


class PersonSexoSerializer(ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'nome', 'sobrenome',
                  'sexo', 'altura', 'peso',
                  'nascimento', 'bairro', 'cidade',
                  'estado', 'numero')
