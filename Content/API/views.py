from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.mixins import RetrieveModelMixin,ListModelMixin,CreateModelMixin,UpdateModelMixin
from .serializers import ContentSerializer
class GetAllContentView(ListAPIView,
                        ListModelMixin):
    serializer_class = ContentSerializer

    def get_queryset(self):
        None
    def get(self, request, *args, **kwargs):
        return self.list(request,*args,**kwargs)

# Create your views here.
