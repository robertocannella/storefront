# Create your views here.
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response



@api_view()
def routine_list(request):
    return Response("hello")

@api_view()
def routine_detail(request, id):
    return Response("hello")