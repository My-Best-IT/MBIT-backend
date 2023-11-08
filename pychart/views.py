from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from .models import Mbit
from .serializers import MbitSerializer

# Create your views here.

@api_view(['GET', 'POST'])
def MbitAPI(request):
    if request.method == 'GET':
        mbits = Mbit.objects.all()
        serializer = MbitSerializer(mbits, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = MbitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def MbitAPIS(request, frontend, backend, data, game, security):
    mbit = get_object_or_404(Mbit, frontend=frontend, backend=backend, data=data, game=game, security=security)
    serializer = MbitSerializer(mbit)
    return Response(serializer.data, status=status.HTTP_200_OK)
