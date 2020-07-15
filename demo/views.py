# from django.shortcuts import render
# from django.http import HttpResponse
# from django.views import View
# from django.shortcuts import render

from .models import Book
from rest_framework import viewsets
from .serializers import BookSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)



# def first(request):
#     books = Book.objects.all()
#     return render(request, 'first_temp.html', {'books': books})
#
# class Another(View):
#
#     Books = Book.objects.filter(is_published=True)
#     output = ''
#     for book in Books:
#         output += f"This book title {book.title} is published<br>"
#
#     def get(self, request):
#         return HttpResponse(self.output)


