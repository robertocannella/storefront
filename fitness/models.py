from django.db import models
from django.utils import timezone

class ExerciseLog(models.Model):
    date = models.DateField(default=timezone.now)
    name = models.CharField(max_length=100, unique=True)

    def save(self, *args, **kwargs):
        if not self.id:  # If this is a new object (not yet saved to the database)
            self.name = self.date.strftime('%Y-%m-%d')
            if ExerciseLog.objects.filter(name=self.name).exists():
                counter = 2
                while ExerciseLog.objects.filter(name=f"{self.name}-{counter}").exists():
                    counter += 1
                self.name = f"{self.name}-{counter}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class ExerciseSession(models.Model):
    log = models.ForeignKey(ExerciseLog, related_name='sessions', on_delete=models.CASCADE)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Session on {self.log.date} at {self.start_time.time()}"

class ExerciseSet(models.Model):
    session = models.ForeignKey(ExerciseSession, related_name='exercise_sets', on_delete=models.CASCADE)
    exercise_name = models.CharField(max_length=100)
    repetitions = models.IntegerField()
    sets = models.IntegerField()

    def __str__(self):
        return f"{self.exercise_name}: {self.sets} sets of {self.repetitions} reps"
