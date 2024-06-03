from django.urls import path
from .views import AddBookApi, BookListApi, BookDetailApi, DeleteBookApi, UpdateBookApi

urlpatterns = [
    path('create-book/', AddBookApi.as_view(), name='create_book'),
    path('book-list/', BookListApi.as_view(), name='book_list'),
    path('book-detail/<int:pk>/', BookDetailApi.as_view(), name='book_detail'),
    path('book-delete/', DeleteBookApi.as_view(), name='book_delete'),
    path('book-update/', UpdateBookApi.as_view(), name='book_update'),
]
