

# Register your models here.
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import FoodTable
# Register your models here.



@admin.register(FoodTable)
class FoodModelAdmin(admin.ModelAdmin):
    list_display=['id','OrderDate','Region','City','Category','Product','Quantity','UnitPrice']


    