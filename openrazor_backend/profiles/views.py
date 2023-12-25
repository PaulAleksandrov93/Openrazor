from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .models import UserProfile
from .serializers import UserProfileSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token',
        '/api/token/refresh',
    ]
    
    return Response(routes)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_profiles(request):
    profiles = UserProfile.objects.all()
    serializer = UserProfileSerializer(profiles, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_profile(request, pk):
    profile = UserProfile.objects.get(id=pk)
    serializer = UserProfileSerializer(profile)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_user_profile(request):
    serializer = UserProfileSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user_profile(request, pk):
    profile = UserProfile.objects.get(id=pk)
    serializer = UserProfileSerializer(instance=profile, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_user_profile(request, pk):
    profile = UserProfile.objects.get(id=pk)
    profile.delete()
    return Response('Профиль успешно удален!', status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({'error': 'Username and password are required.'}, status=400)

    user = User.objects.create_user(username=username, password=password)
    user_profile_serializer = UserProfileSerializer(data={'user': user.id})
    
    if user_profile_serializer.is_valid():
        user_profile_serializer.save()
        return Response({'message': 'User registered successfully.'}, status=201)

    user.delete()
    return Response({'error': 'Registration failed.', 'details': user_profile_serializer.errors}, status=400)