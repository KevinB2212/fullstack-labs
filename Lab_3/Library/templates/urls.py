from django.urls import path
from . import views
from .views import *

urlpatterns = [
   path('', index, name='base.html'),
   path('books/', view_all_books, name='all_books'),
   path('books/<int:bookid>/', view_single_book, name='single_book'),
   path('books/year/<int:year>/', books_in_year, name='books_in_year'),
   path('books/category/<str:category>/year/<int:year>/', BooksByCategoryAndYearView.as_view(), name='books_by_category_and_year'),
   path('category/<str:category>/', BooksByCategoryView.as_view(), name='books_by_category'),
]