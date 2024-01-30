from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404
from django.views.generic import ListView


def index(request):
    years_range = range(2000, 2030)
    return render(request, 'base.html', {'years_range': years_range})

def view_all_books(request):
    all_books = Book.objects.all()
    return render(request, 'all_books.html', {'books':all_books})

def view_single_book(request, bookid):
    single_book = get_object_or_404(Book, id=bookid)
    return render(request, 'single_book.html', {'book':single_book})

def books_in_year(request, year):
    books = Book.objects.filter(year=year)
    context = {'books': books, 'year': year}
    return render(request, 'books_in_year.html', context)

class BooksByCategoryView(ListView):
    model = Book
    template_name = 'books/books_by_category.html'
    context_object_name = 'books'

    def get_queryset(self):
        category = self.kwargs['category']
        return Book.objects.filter(category=category)

class BooksByCategoryAndYearView(ListView):
    model = Book
    template_name = 'books_by_category_and_year.html'
    context_object_name = 'book_list'

    def get_queryset(self):
        category = self.kwargs['category']
        year = self.kwargs['year']
        queryset = Book.objects.filter(category=category, year=year)
        return queryset