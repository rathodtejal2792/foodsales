from import_export import resources
from .models import FoodTable


class FoodTableResource(resources.ModelResource):
    class meta:
        model=FoodTable