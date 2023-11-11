from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404
from .models import Mbit
from .serializers import MbitSerializer

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

class MbitViewSet(viewsets.ModelViewSet):
    queryset = Mbit.objects.all()
    serializer_class = MbitSerializer

    @action(detail=True, methods=['patch'])
    def increment_values(self, request, pk=None):
        instance = self.get_object()

        # Get the values from the request data
        frontend = int(request.data.get('frontend', 0))
        backend = int(request.data.get('backend', 0))
        game = int(request.data.get('game', 0))
        security = int(request.data.get('security', 0))
        data = int(request.data.get('data', 0))

        # Increment the values
        instance.frontend += frontend
        instance.backend += backend
        instance.game += game
        instance.security += security
        instance.data += data

        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
