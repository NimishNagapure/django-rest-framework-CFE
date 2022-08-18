from asyncore import read
from dataclasses import field
import email
from urllib import request
from rest_framework import serializers
from .models import Product
from rest_framework.reverse import reverse
from .validators import validate_title_no_hello, unique_product_title
from api.serializers import UserPublicSerializer

class ProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='product-details',
        lookup_field='pk',
        read_only=True
    )
    title = serializers.CharField(read_only=True)

class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source= 'user',read_only=True)
    related_product=ProductInlineSerializer(source='user.product_set.all',many = True,read_only=True)
    discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name="product-details", lookup_field="pk"
    )
    # email= serializers.EmailField(write_only=True)
    title = serializers.CharField(
        validators=[validate_title_no_hello, unique_product_title]
    )
    name = serializers.CharField(source="title", read_only=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "price",
            "content",
            "sale_price",
            "discount",
            "edit_url",
            "url",
            "name",
            "owner",
            "related_product",
        ]

    def validate_title(self, value):
        request = self.context.get("request")
        user = request.user

        qs = Product.objects.filter(user=user, title__iexact=value)
        if qs.exists():
            raise serializers.ValidationError(
                f"{value} This title has already been used"
            )
        return value

    # def create(self, validated_data):
    #     # return Product.objects.create(validated_data)
    #     # email = validated_data.pop('email')
    #     obj= super().create(validated_data)
    #     # print(obj,email)
    #     return obj

    # def update(self, instance, validated_data):
    #     email = validated_data.pop('email')
    #     # instance.title = validated_data.get('title', instance.title)

    # return super().update(instance, validated_data)
    def get_edit_url(self, obj):
        # return f"/api/products/{obj.id}"
        request = self.context.get("request")
        if request is None:
            return None
        return reverse("product-edit", kwargs={"pk": obj.pk}, request=request)

    # def get_discount(self,obj):
    #     try:
    #         return obj.discount_price()
    #     except:
    #         return None

    def get_discount(self, obj):
        # to hedge this, obj
        if not hasattr(obj, "id"):
            return None
        if not isinstance(obj, Product):
            return None

        return obj.discount_price()
