from typing import Any
from django.contrib import admin, messages
from django.db.models.query import QuerySet
from django.http import HttpRequest
from django.utils.html import format_html, urlencode
from django.urls import reverse

from tag.models import TaggedItem
from . import models
from django.db.models import Count

    
@admin.register(models.ExerciseLog)
class ExerciseLog(admin.ModelAdmin):
    list_display= ['log_id','name']

@admin.register(models.ExerciseType)
class ExerciseType(admin.ModelAdmin):
    list_display = [ 'id','name']
    list_editable = ['name']

    
@admin.register(models.ExerciseRoutine)
class ExerciseLogMeta(admin.ModelAdmin):
    list_display = [  'date', 'start_time', 'end_time', 'description']

@admin.register(models.Units)
class ExerciseLogMeta(admin.ModelAdmin):
    list_display = [  'name' ]

@admin.register(models.EquipmentType)
class ExerciseLogMeta(admin.ModelAdmin):

    list_display = [ 'name']

