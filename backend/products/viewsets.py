from itertools import product
from rest_framework import viewsets, mixins, status
from .models import  Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):

    """
    get --> list --> QuerySet
    post --> create --> new instance
    get --> retrieve --> product instance detail view
    put --> update --> product instance detail view
    patch --> partial update --> product instance detail view
    delete --> destroy --> product instance detail view

    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'id'

class ProductGenericViewSet(viewsets.GenericViewSet,
                            mixins.ListModelMixin,mixins.RetrieveModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'id'

product_list_view = ProductGenericViewSet.as_view({
    'get':'list'})
product_detail_view = ProductGenericViewSet.as_view({
    'get':'retrieve'})