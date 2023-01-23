from django.shortcuts import render
from .models import FoodTable
from .resources import FoodTableResource
from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponse

from rest_framework.generics import ListAPIView
from .serializers import FoodTableSerializer
from  rest_framework.filters import SearchFilter
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# Create your views here.



def simple_upload(request):
    if request.method=='POST':
        food_resource=FoodTableResource()
        dataset=Dataset()
        new_file=request.FILES['myfile']

        if not new_file.name.endswith('xlsx'):
            messages.info(request,'wrong format')
            return render(request,'food/upload.html')

        imported_data=dataset.load(new_file.read(),format='xlsx')
        for data in imported_data:
           
            value=FoodTable(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7])
            

            value.save()

    return render(request,'food/upload.html')



class ListTodoAPIView(ListAPIView):
    """This endpoint list all of the available todos from the database"""
    queryset = FoodTable.objects.all()
    serializer_class = FoodTableSerializer
    filter_backends=[SearchFilter]
    search_fields=['Product']

    