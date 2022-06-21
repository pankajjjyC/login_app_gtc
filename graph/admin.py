from django.contrib import admin
from .models import Heath_Record,Csv
@admin.register(Heath_Record)
class Health_RecordAdmin(admin.ModelAdmin):
   list_display=['id','average_pulse','calorie_burnage']
@admin.register(Csv)
class CsvAdmin(admin.ModelAdmin):
   list_display=['id','csv']