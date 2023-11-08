from .views import MbitAPI
from django.urls import path,include

from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("pychart/", include("pychart.urls")),
]


urlpatterns =[
    path("fbv/mbits",MbitAPI),
]