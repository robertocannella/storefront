from django.db import models
from django.utils import timezone

class ExerciseSession(models.Model):
    date = models.DateField(default=timezone.now)
    name = models.CharField(max_length=100, unique=True)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.id:  # If this is a new object (not yet saved to the database)
            self.name = self.date.strftime('%Y-%m-%d')
            if ExerciseSession.objects.filter(name=self.name).exists():
                counter = 2
                while ExerciseSession.objects.filter(name=f"{self.name}-{counter}").exists():
                    counter += 1
                self.name = f"{self.name}-{counter}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Unit(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class EquipmentType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class ExerciseType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Exercise(models.Model):
    session = models.ForeignKey(ExerciseSession, related_name='exercises', on_delete=models.CASCADE)
    exercise_type = models.ForeignKey(ExerciseType, related_name='exercises', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.exercise_type.name} (Session: {self.session.name})"

class ExerciseSet(models.Model):
    exercise = models.ForeignKey(Exercise, related_name='sets', on_delete=models.CASCADE)
    repetitions = models.IntegerField()
    weight = models.FloatField(null=True, blank=True)
    weight_unit = models.ForeignKey(Unit, related_name='weight_unit', null=True, blank=True, on_delete=models.SET_NULL)
    equipment_type = models.ForeignKey(EquipmentType, null=True, blank=True, on_delete=models.SET_NULL)
    duration = models.DurationField(null=True, blank=True)
    duration_unit = models.ForeignKey(Unit, related_name='duration_unit', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.exercise.exercise_type.name}: {self.repetitions} reps"
