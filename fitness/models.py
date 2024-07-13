from django.db import models

# Create your models here.
class ExerciseType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name = "Exercise Type"
        verbose_name_plural = "Exercise Types"


class ExerciseRoutine(models.Model):
    log_id = models.AutoField(primary_key=True)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    description = models.TextField()


    def __str__(self) -> str:
        return str(self.log_id)
    
    class Meta:
        verbose_name = "Exercise Routine"
        verbose_name_plural = "Exercise Routines"


class EquipmentType(models.Model):
    equip_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Equipment"
        verbose_name_plural = "Equipment"

class Units(models.Model):
    units_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Units"
        verbose_name_plural = "Units"

class ExerciseLog(models.Model):
    log_id = models.ForeignKey(ExerciseRoutine, on_delete=models.CASCADE)
    exercise_id = models.ForeignKey(ExerciseType, on_delete=models.PROTECT)
    equip_id = models.ForeignKey(EquipmentType, on_delete=models.PROTECT)
    name = models.CharField(max_length=255)     