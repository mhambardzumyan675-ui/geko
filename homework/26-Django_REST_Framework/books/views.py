from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
from django.db.models import Avg, Sum

@api_view(['POST'])
def create_book(request):
  serializer=BookSerializer(data=request.data)
  if serializer.is_valid():
     serializer.save()
     return Response(serializer.data,status=status.HTTP_201_CREATED)
  return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_books(request):
    books = Book.objects.all()
    if not books.exists():
       return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = BookSerializer(books,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def book_details(request,book_id):
   try:
       book=Book.objects.get(id=book_id)
   except Book.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)
   
   serializer=BookSerializer(book)
   return Response(serializer.data,status=status.HTTP_200_OK)
   
@api_view(['PUT'])
def update_book(request,book_id):
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = BookSerializer(book, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_book(request,book_id):
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return Response({'message':'NOT FOUND'},status=status.HTTP_404_NOT_FOUND)
    book.delete()
    return Response(
        status=status.HTTP_204_NO_CONTENT
        )

@api_view(['GET'])
def search_books(request):

    author = request.GET.get("author")

    books = Book.objects.filter(author__icontains=author)

    serializer = BookSerializer(books, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def largest_book(request):
    book = Book.objects.order_by("-pages").first()
    if not book:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = BookSerializer(book)
    return Response(serializer.data)

@api_view(['GET'])
def statistics(request):
    books = Book.objects.all()
    data = {
        "total_books": books.count(),
        "total_pages": books.aggregate(Sum("pages"))["pages__sum"] or 0,
        "average_pages": books.aggregate(Avg("pages"))["pages__avg"] or 0,
        "available_books": books.filter(is_available=True).count(),
        "unavailable_books": books.filter(is_available=False).count(),
    }
    return Response(data)