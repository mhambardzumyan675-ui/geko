from .views import create_book,get_books,book_details,update_book,delete_book,search_books,largest_book,statistics
from django.urls import path

urlpatterns=[
path('create/',create_book),
path('get/',get_books),
path('get/<int:book_id>/',book_details),
path('update/<int:book_id>/',update_book),
path('delete/<int:book_id>/',delete_book),
path('search/',search_books),
path('largest/',largest_book),
path('statistics/',statistics),

]