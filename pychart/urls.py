from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MbitAPI, MbitAPIS, MbitViewSet  # Ensure this import is correct

router = DefaultRouter()
router.register(r'mbits', MbitViewSet, basename='mbit')

urlpatterns = [
    path('fbv/mbits/', MbitAPI),
    path('fbv/mbits/<str:frontend>/<str:backend>/<str:data>/<str:game>/<str:security>/', MbitAPIS, name='mbit-apis'),
    path('', include(router.urls)),
]
