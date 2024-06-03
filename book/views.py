from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BookSerializer
from user.models import User
from rest_framework import status
from .models import Book


# Create your views here.


class AddBookApi(APIView):
    def post(self, request):
        title = request.data.get('title')
        description = request.data.get('description')
        author = request.data.get('author')
        year = request.data.get('year')
        pages = request.data.get('pages')
        username = request.data.get('username')

        # Get the user object
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        # Create the book object
        book = Book.objects.create(
            title=title,
            description=description,
            author=author,
            year=year,
            pages=pages,
            user=user
        )

        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class BookListApi(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


class BookDetailApi(APIView):
    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        book = self.get_object(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)


class DeleteBookApi(APIView):
    def delete(self, request):
        book_id = request.data.get('id')
        username = request.data.get('username')

        user = User.objects.get(username=username)
        book = Book.objects.get(pk=book_id)
        if book.user != user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        else:
            book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class UpdateBookApi(APIView):
    def put(self, request):
        try:
            book_id = request.data.get('id')
            title = request.data.get('title')
            description = request.data.get('description')
            author = request.data.get('author')
            year = request.data.get('year')
            pages = request.data.get('pages')
            username = request.data.get('username')

            user = User.objects.get(username=username)
            book = Book.objects.get(pk=book_id)

            if book.user != user:
                return Response(status=status.HTTP_403_FORBIDDEN)

            book.title = title
            book.description = description
            book.author = author
            book.year = year
            book.pages = pages
            book.save()

            return Response(status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        except Book.DoesNotExist:
            return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
