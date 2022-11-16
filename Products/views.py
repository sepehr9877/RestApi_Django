import json

from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
from .permissions import IsOwnerOrReadOnly
# Create your views here.
from rest_framework import status, generics, permissions,mixins
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
class ProductSearch(APIView):
    def get_queryset(self,request,*args,**kwargs):
        search=self.request.Get.get('q')
        selected_product=Products.objects.filter(title__contains=search).all()
        return search

class ProductPage(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly
                          ]
    def get(self,*args,**kwargs):
        search=self.request.Get.get('q')
        if search :
            return Products.objects.filter(title__contains=search).all()
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
    def get_queryset(self):
        search=self.request.GET.get('q')
        if search:
            self.queryset=Products.objects.filter(title__contains=search).all()
        return self.queryset

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
###Creating An EndPoint For CRUD


class ProductUserEndPoint(generics.ListAPIView,
                          mixins.RetrieveModelMixin,
                          mixins.UpdateModelMixin,
                          mixins.DestroyModelMixin,
                          mixins.CreateModelMixin):
    lookup_field = ['q','ID']
    serializer_class =ProductuserSerializer
    queryset = Products.objects.all()
    passed_id=None
    def get_queryset(self):
        search=self.request.GET.get('q')
        searched_item=Products.objects.all()
        if search:
            searched_item=searched_item.filter(title__icontains=search).all()

        return searched_item
    def get_object(self):
        id=self.request.GET.get('id')
        obj=None
        if id:
            obj=self.queryset.get(id=id)
        if self.passed_id:
            obj=self.queryset.get(id=self.passed_id['id'])
        return obj
    def is_json(self,mydata):
        try:
            json_object=json.loads(mydata)
        except ValueError as e:
            return False
        return True
    def get(self, request, *args, **kwargs):
        self.passed_id=self.request.GET.get('id')
        json_data=None
        print(self.request.body)
        if self.is_json(self.request.body):
            json_data=json.loads(self.request.body)
            self.passed_id=json_data
        if self.passed_id is not None:
            return self.retrieve(request, *args, **kwargs)
        return super().get(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def delete(self,request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

