from django.contrib import admin
from django.forms.models import BaseInlineFormSet
from .models import ExerciseSession, Unit, EquipmentType, ExerciseType, Exercise, ExerciseSet

class ExerciseSetInlineFormSet(BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        super(ExerciseSetInlineFormSet, self).__init__(*args, **kwargs)
        for i in range(3 - len(self.forms)):
            self.forms.append(self._construct_form(i))

class ExerciseSetInline(admin.TabularInline):
    model = ExerciseSet
    formset = ExerciseSetInlineFormSet
    extra = 3

class ExerciseInline(admin.TabularInline):
    model = Exercise
    extra = 1
    inlines = [ExerciseSetInline]

class ExerciseSessionAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'start_time', 'end_time')
    inlines = [ExerciseInline]

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(EquipmentType)
class EquipmentTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(ExerciseType)
class ExerciseTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('exercise_type', 'session')
    inlines = [ExerciseSetInline]

@admin.register(ExerciseSet)
class ExerciseSetAdmin(admin.ModelAdmin):
    list_display = ('exercise', 'repetitions', 'weight', 'weight_unit', 'equipment_type', 'duration', 'duration_unit')

@admin.register(ExerciseSession)
class ExerciseSessionAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'start_time', 'end_time')
    inlines = [ExerciseInline]
