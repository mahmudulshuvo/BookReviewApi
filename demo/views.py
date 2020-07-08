from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

def first(request):
    return HttpResponse('First message from views')

class Another(View):
    def get(self, request):
        return HttpResponse('This is another function inside class')
