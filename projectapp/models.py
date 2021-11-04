from django.db import models

# Create your models here.

SEXO_CHOICES = (
    ('M', 'masculino'),
    ('F', 'feminino'),
)


class Person(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50, null=True, blank=True)
    sexo = models.CharField(max_length=2, choices=SEXO_CHOICES)
    altura = models.FloatField(null=True, blank=True, default=None)
    peso = models.FloatField(null=True, blank=True, default=None)
    nascimento = models.DateTimeField(verbose_name="Data de Nascimento", null=True)
    bairro = models.CharField(max_length=30)
    cidade = models.CharField(max_length=20)
    estado = models.CharField(max_length=20)
    numero = models.DecimalField(max_digits=8, decimal_places=0)

    def __str__(self):
        return self.nome

    def get_nascimento(self):
        return self.nascimento.strftime('%d/%m/%Y')
