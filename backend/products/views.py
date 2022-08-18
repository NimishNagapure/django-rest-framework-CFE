from cgitb import lookup
from django import views
from rest_framework import generics,mixins ,authentication
from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from rest_framework.http import Http404
from django.shortcuts import get_object_or_404
# from api.permissions import IsStaffEditorPermission
# from api.authentication import TokenAuthentication
from api.mixins import StaffEditorPermissionMixin

class ProductListAPIView(StaffEditorPermissionMixin,generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'id'

product_list_view = ProductListAPIView.as_view()

class ProductListCreateAPIView(StaffEditorPermissionMixin,generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # authentication_classes = [TokenAuthentication] 
    # permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):

        # serializer.save(user=self.request.user)
        # email = serializer.validated_data.pop('email')
        print(serializer.validated_data)
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content")
        # or None
        if content is  None:
            content = title
        serializer.save(user = self.request.user,content=content)
        #if its not directly related to model then send a signal 

    # def get_queryset(self, *args, **kwargs):
    #     qs = super().get_queryset(*args, **kwargs)
    #     request = self.request
    #     # print(request.user)
    #     user = request.user
    #     if user.is_authenticated:
    #         return Product.objects.none()
    #     return qs.filter(user=request.user)

product_list_create_view = ProductListCreateAPIView.as_view()

class ProductDetailsAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'id'

product_details_view = ProductDetailsAPIView.as_view()


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    
    def perform_update(self, serializer):
        instance  = serializer.save()
        if not instance.content:
            instance.content = instance.title
                

product_update_view = ProductUpdateAPIView.as_view()

class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    
    def perform_destroy(self, instance):
        #instance
        super().perform_destroy(instance)
        

product_delete_view = ProductDeleteAPIView.as_view()

# class CreateProductAPIView(mixins.CreateModelMixin,generics.CreateAPIView):
#     pass
  
class ProductMixinView(mixins.CreateModelMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get(self,request,*args,**kwargs):
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request,*args,**kwargs)
        return self.list(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)


    def perform_create(self, serializer):

        # serializer.save(user=self.request.user)
        print(serializer.validated_data)
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content") or None
        # or None
        if content is  None:
            content = "This single view doing cool stuff"
        serializer.save(content=content)
        #if its not directly related to model then send a signal
product_mixin_view = ProductMixinView.as_view()

@api_view(['GET',"POST"])
def product_alt_view(request,pk=None,*args, **kwargs):
    method = request.method

    if method == "GET":
        if pk is not None:
            # # detail view
            # queryset = Product.objects.all()
            # if not queryset.exists():
            #     return Response({"message":"Product not found"},status=404)
            obj = get_object_or_404(Product,pk=pk)
            data = ProductSerializer(obj,many = False).data
            return Response(data)



        # url_args ??
        # get request --> detail views


        else:
            # list view 
            queryset=Product.objects.all()
            data = ProductSerializer(queryset,many=True).data
            return Response(data)

    if method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get("title")
            content = serializer.validated_data.get("content")
            # or None
            if content is  None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)