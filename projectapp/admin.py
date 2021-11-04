from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from projectapp.models import Person


# Register your models here.

@admin.register(Person)
# admin.site.register(Person)
class PersonAdmin(ImportExportModelAdmin):
    list_display = ('nome', 'sobrenome', 'sexo',
                    'altura', 'peso', 'nascimento',
                    'bairro', 'cidade', 'estado', 'numero')
    # list_filter = ('nome',)

# class PersonAdmin(admin.ModelAdmin):
#     list_display = ('__all__',)
