import logging
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Category
from .serializers import CategorySerializer

logger = logging.getLogger(__name__)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getCategories(request):
    try:
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    except Exception as e:
        logger.error(f'Произошла ошибка во время выполнения getCategories: {e}', exc_info=True)
        return Response({'error': 'Внутренняя ошибка сервера'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getCategory(request, pk):
    try:
        category = Category.objects.get(id=pk)
        serializer = CategorySerializer(category, many=False)
        return Response(serializer.data)
    except Category.DoesNotExist:
        return Response({'error': 'Категория не найдена'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        logger.error(f'Произошла ошибка во время выполнения getCategory: {e}', exc_info=True)
        return Response({'error': 'Внутренняя ошибка сервера'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def createCategory(request):
    try:
        serializer = CategorySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        logger.error(f'Произошла ошибка во время выполнения createCategory: {e}', exc_info=True)
        return Response({'error': 'Внутренняя ошибка сервера'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['PUT'])
# @permission_classes([IsAuthenticated])
def updateCategory(request, pk):
    try:
        category = Category.objects.get(id=pk)
        serializer = CategorySerializer(instance=category, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Category.DoesNotExist:
        return Response({'error': 'Категория не найдена'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        logger.error(f'Произошла ошибка во время выполнения updateCategory: {e}', exc_info=True)
        return Response({'error': 'Внутренняя ошибка сервера'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['DELETE'])
# @permission_classes([IsAuthenticated])
def deleteCategory(request, pk):
    try:
        category = Category.objects.get(id=pk)
        category.delete()
        return Response('Категория успешно удалена!', status=status.HTTP_204_NO_CONTENT)
    except Category.DoesNotExist:
        return Response({'error': 'Категория не найдена'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        logger.error(f'Произошла ошибка во время выполнения deleteCategory: {e}', exc_info=True)
        return Response({'error': 'Внутренняя ошибка сервера'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
