from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import SocialNetwork
from .serializers import SocialNetworkSerializer

@api_view(['GET', 'POST'])
def social_network_list(request):
    if request.method == 'GET':
        social_networks = SocialNetwork.objects.all()
        serializer = SocialNetworkSerializer(social_networks, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SocialNetworkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def social_network_detail(request, pk):
    try:
        social_network = SocialNetwork.objects.get(pk=pk)
    except SocialNetwork.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SocialNetworkSerializer(social_network)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SocialNetworkSerializer(social_network, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        social_network.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)