from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book
from django.shortcuts import render

def first(request):
    books = Book.objects.all()
    return render(request, 'first_temp.html', {'books': books})

class Another(View):

    Books = Book.objects.filter(is_published=True)
    output = ''
    for book in Books:
        output += f"This book title {book.title} is published<br>"

    def get(self, request):
        return HttpResponse(self.output)
