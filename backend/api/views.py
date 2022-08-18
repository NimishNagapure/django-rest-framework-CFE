from email import header
from itertools import product
from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render
import json
# Create your views here.
# from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.models import Product
from django.forms.models import model_to_dict
from products.serializers import ProductSerializer

@api_view(['POST'])
def api_home(request,*args, **kwargs):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        # print(instance)
        data = serializer.data
        return Response(data)
    # return Response({"error":"Invalid data"},status=400)
    """    
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        data = ProductSerializer(instance).data

    return Response(data)
    """

    """
    model_data = Product.objects.all().order_by("?").first() # get a random queryset and grab one of those values
    data = {}
    # if model_data:
    #     data['id'] = model_data.id
    #     data['title'] = model_data.title
    #     data['price'] = model_data.price
    #     data['content'] = model_data.content     
    if model_data:
        data = model_to_dict(model_data,fields=['id','title',"price","sale_price"])
    return Response(data)
        # print(data)
        # json_data = json.dumps(data)
    # return JsonResponse(json_data,headers={"content-type":"application/json"})
    """
    
    """
    # # request ---> HttpRequest ---> Django
    # # print(dir(request))
    # # request.body 
    # print(request.GET)
    # body = request.body # byte string of the json data
    # data = {}
    # try:
    #     data = json.loads(body) # convert byte string to python dictionary
    # except:
    #     pass

    # # print(data)
    # data['params'] = request.GET

    # data['headers'] = dict(request.headers)
    # # print(request.headers)
    # data['method'] = request.method
    # data['content_type'] = request.content_type
    # return JsonResponse(data)
    """


