from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ExerciseRoutine
from .serializers import ExerciseLogMetaSerializer



# Create your views here.
@api_view()
def exercise_list(request):
    query_set = ExerciseRoutine.objects.all()
    serializer = ExerciseLogMetaSerializer(query_set, many=True)
    return Response(serializer.data)

@api_view()
def exercise_detail(request, id):
    product = get_object_or_404(ExerciseLog, pk=id)
    serializer = ExerciseLogMetaSerializer(product)
    return Response(serializer.data)