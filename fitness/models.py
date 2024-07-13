from django.db import models

# Create your models here.
class ExerciseType(models.Model):
    name = models.CharField(max_length=255)

# Create your models here.
class ExerciseLog(models.Model):
    log_id = models.PositiveSmallIntegerField(primary_key=True, unique=True)
    date = models.DateField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    description = models.TextField()


# class ExerciseLogMeta(models.Model):
#      name = models.CharField(max_length=255)

# class EquipmentType(models.Model):
#      name = models.CharField(max_length=255)

# class Units(models.Model):
#      name = models.CharField(max_length=255)