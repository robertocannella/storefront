from rest_framework import serializers
from .models import ExerciseRoutine
from decimal import Decimal, ROUND_HALF_UP

class ExerciseLogMetaSerializer(serializers.Serializer):
    log_id = serializers.IntegerField()
    date = serializers.DateField()
    start_time = serializers.DateTimeField()
    end_time = serializers.DateTimeField()
    description = serializers.CharField()

