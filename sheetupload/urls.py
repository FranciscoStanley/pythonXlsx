"""sheetupload URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls import include
from rest_framework import routers

from projectapp import views
from projectapp.api.viewsets import PersonViewSet, PersonSexoViewSet

router = routers.DefaultRouter()
router.register(r'meeren', PersonViewSet, basename='Person')
router.register(r'sexo', PersonSexoViewSet, basename='PersonSexo')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('projectapp.urls', namespace='projectapp')),
    path('export/', views.export),
    path('person/', include(router.urls)),
    path('mereen/', include(router.urls)),
    path('sexo/', include(router.urls)),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
