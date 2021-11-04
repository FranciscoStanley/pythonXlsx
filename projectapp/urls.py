from django.urls import path
from .views import simple_upload

app_name = 'projectapp'

urlpatterns = [
    path('', simple_upload, name='upload-view'),
]