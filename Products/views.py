from django.contrib.auth.models import User
from django.shortcuts import render
from .permissions import IsOwnerOrReadOnly
# Create your views here.
from rest_framework import status, generics, permissions
from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from .models import Products
from .serializers import ProductSerializer,ProductuserSerializer
# Function Base view
# @api_view(['GET','POST'])
# def ProductsViews(request):
#     products=None
#     serializers=None
#     if request.method=="GET":
#         products=Products.objects.all()
#         serializers=ProductSerializer(products,many=True)
#         return Response(serializers.data)
#     elif request.method=="POST":
#         serializers=ProductSerializer(data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data,status=status.HTTP_201_CREATED)
#         return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
# @api_view(['GET','POST'])
# def ProdcutsViewDetail(request,*args,**kwargs):
#     id=kwargs["ID"]
#     try:
#        selected_products=Products.objects.get(id=id)
#     except selected_products.DoesNotExist:
#         return Response(status=status.HTTP_400_BAD_REQUEST)
#     if request.method=="GET":
#         json_pro=ProductSerializer(selected_products)
#         return Response(json_pro.data)

##ClassBaseView
class ProductPage(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly
                          ]
    def get(self,*args,**kwargs):
        products=Products.objects.all()
        serializer=ProductSerializer(products,many=True)
        return Response(serializer.data)
    def perform_create(self,serlializer):
        serlializer.save(owner=self.request.user)
    def post(self,request,format=None):
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class ProductDetail(APIView):

    def get_object(self,*args,**kwargs):
        id=self.kwargs["ID"]
        selected_product=Products.objects.get(id=id)
        print("get_object")
        print(selected_product)
        queryset=selected_product
        return queryset
    def get(self,*args,format=None,**kwargs):
        queryset=self.get_object()
        serializer=ProductSerializer(queryset)
        print("get")
        print(serializer.data)
        return Response(serializer.data)
###Retreive Items and Create them before adding user to Products Model
class ProMixin(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
class ProdetailMixin(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
##Now We Only want to Read products with new serializer
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = ProductuserSerializer
class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = ProductuserSerializer
