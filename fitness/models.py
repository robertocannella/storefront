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
    log = models.AutoField(primary_key=True)
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
    equip = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Equipment"
        verbose_name_plural = "Equipment"

class Units(models.Model):
    units = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Units"
        verbose_name_plural = "Units"

class ExerciseLog(models.Model):
    routine = models.ForeignKey(ExerciseRoutine, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)  
    
    
class ExerciseSet(models.Model):
    set = models.AutoField(primary_key=True)
    log = models.ForeignKey(ExerciseRoutine, on_delete=models.CASCADE)
    equipment = models.ForeignKey(EquipmentType, on_delete=models.PROTECT)
    sequence_no = models.PositiveSmallIntegerField()
    weight = models.PositiveBigIntegerField()
    repetitions = models.PositiveSmallIntegerField()
    units = models.ForeignKey(Units, on_delete=models.PROTECT)
    duration = models.PositiveSmallIntegerField(null=True)


