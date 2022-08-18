from rest_framework import serializers
from .models import Product
from rest_framework.validators import UniqueValidator

 
 
# def validate_title(value):
#     qs = Product.objects.filter(title__iexact=value)
#     if qs.exists():
#         raise serializers.ValidationError(f"{value} This title has already been used")
#     return value


def validate_title_no_hello(value):
    if "hello" in value.lower():
        raise serializers.ValidationError("This title is not allowed to start with Hello")
    return value

unique_product_title = UniqueValidator(
    queryset=Product.objects.all())