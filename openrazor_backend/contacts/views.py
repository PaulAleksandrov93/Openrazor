from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import StoreContact
from .serializers import StoreContactSerializer

@api_view(['GET'])
def store_contact_detail(request):
    contact = StoreContact.objects.first()
    serializer = StoreContactSerializer(contact)
    return Response(serializer.data)

@api_view(['GET'])
def store_contact_list(request):
    contacts = StoreContact.objects.all()
    serializer = StoreContactSerializer(contacts, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def store_contact_create(request):
    serializer = StoreContactSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def store_contact_detail_api(request, pk):
    try:
        contact = StoreContact.objects.get(pk=pk)
    except StoreContact.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StoreContactSerializer(contact)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StoreContactSerializer(contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)