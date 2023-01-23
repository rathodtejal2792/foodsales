from django.db import models

# Create your models here.
class FoodTable(models.Model):
    OrderDate=models.DateField()
    Region=models.CharField(max_length=200)
    City=models.CharField(max_length=200)
    Category=models.CharField(max_length=200)
    Product=models.CharField(max_length=200)
    Quantity=models.IntegerField(default=0)
    UnitPrice= models.DecimalField(default=0,max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.Product)




