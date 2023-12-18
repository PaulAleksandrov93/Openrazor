import logging

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.db.models import Q


from .models import Product
from .serializers import ProductSerializer

logger = logging.getLogger(__name__)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getProducts(request):
    try:
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    except Exception as e:
        logger.error(f'Произошла ошибка во время выполнения getProducts: {e}', exc_info=True)
        return Response({'error': 'Внутренняя ошибка сервера'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getProduct(request, pk):
    try:
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product, many=False)
        return Response(serializer.data)
    except Product.DoesNotExist:
        return Response({'error': 'Продукт не найден'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        logger.error(f'Произошла ошибка во время выполнения getProduct: {e}', exc_info=True)
        return Response({'error': 'Внутренняя ошибка сервера'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def createProduct(request):
    try:
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        logger.error(f'Произошла ошибка во время выполнения createProduct: {e}', exc_info=True)
        return Response({'error': 'Внутренняя ошибка сервера'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['PUT'])
# @permission_classes([IsAuthenticated])
def updateProduct(request, pk):
    try:
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(instance=product, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Product.DoesNotExist:
        return Response({'error': 'Продукт не найден'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        logger.error(f'Произошла ошибка во время выполнения updateProduct: {e}', exc_info=True)
        return Response({'error': 'Внутренняя ошибка сервера'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['DELETE'])
# @permission_classes([IsAuthenticated])
def deleteProduct(request, pk):
    try:
        product = Product.objects.get(id=pk)
        product.delete()
        return Response('Продукт успешно удален!', status=status.HTTP_204_NO_CONTENT)
    except Product.DoesNotExist:
        return Response({'error': 'Продукт не найден'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        logger.error(f'Произошла ошибка во время выполнения deleteProduct: {e}', exc_info=True)
        return Response({'error': 'Внутренняя ошибка сервера'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@api_view(['GET'])
def search_products(request):
    query = request.GET.get('query', '')

    if query:
        # Используем Q-объекты для выполнения поиска по нескольким полям
        search_results = Product.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(tags__icontains=query)
        ).distinct()

        serializer = ProductSerializer(search_results, many=True)
        return JsonResponse(serializer.data, safe=False)

    return JsonResponse({'error': 'No search query provided'}, status=400)

@api_view(['GET'])
def get_category_products(request, category_id):
    try:
        products = Product.objects.filter(category_id=category_id)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': 'Внутренняя ошибка сервера'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_product_in_category(request, category_id, product_id):
    try:
        product = Product.objects.get(id=product_id, category_id=category_id)
        serializer = ProductSerializer(product, many=False)
        return Response(serializer.data)
    except Product.DoesNotExist:
        return Response({'error': 'Товар не найден в указанной категории'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': 'Внутренняя ошибка сервера'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)