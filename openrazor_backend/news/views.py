from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import News
from .serializers import NewsSerializer

@api_view(['GET'])
def get_news(request):
    news = News.objects.all()
    serializer = NewsSerializer(news, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_news_detail(request, pk):
    try:
        news = News.objects.get(id=pk)
        serializer = NewsSerializer(news)
        return Response(serializer.data)
    except News.DoesNotExist:
        return Response({'error': 'News not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def create_news(request):
    serializer = NewsSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_news(request, pk):
    try:
        news = News.objects.get(id=pk)
        serializer = NewsSerializer(instance=news, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except News.DoesNotExist:
        return Response({'error': 'News not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_news(request, pk):
    try:
        news = News.objects.get(id=pk)
        news.delete()
        return Response('News deleted successfully!', status=status.HTTP_204_NO_CONTENT)
    except News.DoesNotExist:
        return Response({'error': 'News not found'}, status=status.HTTP_404_NOT_FOUND)