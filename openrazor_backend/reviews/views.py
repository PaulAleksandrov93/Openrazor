from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Review
from .serializers import ReviewSerializer

@api_view(['GET'])
def get_product_reviews(request, product_id):
    reviews = Review.objects.filter(product_id=product_id)
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_review(request, product_id):
    user = request.user
    data = {
        'product': product_id,
        'user': user.id,
        'text': request.data.get('text', ''),
        'rating': request.data.get('rating', 5),
    }
    serializer = ReviewSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_review(request, review_id):
    review = Review.objects.get(pk=review_id)
    user = request.user
    if user != review.user:
        return Response({'error': 'Вы не можете редактировать этот отзыв.'}, status=status.HTTP_403_FORBIDDEN)
    
    serializer = ReviewSerializer(instance=review, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_review(request, review_id):
    review = Review.objects.get(pk=review_id)
    user = request.user
    if user != review.user:
        return Response({'error': 'Вы не можете удалить этот отзыв.'}, status=status.HTTP_403_FORBIDDEN)
    
    review.delete()
    return Response({'message': 'Отзыв успешно удален.'}, status=status.HTTP_204_NO_CONTENT)