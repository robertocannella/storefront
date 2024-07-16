from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response




# Create your views here.
@api_view()
def session_list(request):

    return Response('<h1>Okay</h1>')

@api_view()
def session_detail(request, id):

    return Response(id)
