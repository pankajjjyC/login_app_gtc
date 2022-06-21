from django.db import models
class Heath_Record(models.Model):
    average_pulse=models.IntegerField()
    calorie_burnage=models.IntegerField()  
    class Meta:
        ordering=['id']
class Csv(models.Model):
    csv=models.FileField() 
    class Meta:
        ordering=['id']