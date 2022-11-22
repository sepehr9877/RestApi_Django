from django.shortcuts import render
from rest_framework.generics import ListAPIView,GenericAPIView
from rest_framework.mixins import RetrieveModelMixin,DestroyModelMixin,ListModelMixin,CreateModelMixin,UpdateModelMixin
from .serializers import ContentSerializer
from ..models import Content
from .permissions import UpdateContentObject
from rest_framework.permissions import IsAdminUser
class GetAllContentView(ListAPIView,
                        ListModelMixin):
    serializer_class = ContentSerializer
    permission_classes = (IsAdminUser,)
    def get_queryset(self):
        all_content=Content.objects.all()
        return all_content
    def get(self, request, *args, **kwargs):
        return self.list(request,*args,**kwargs)
class UpdateContent(ListAPIView,
                    RetrieveModelMixin,
                    UpdateModelMixin,
                    DestroyModelMixin
                    ):
    permission_classes = (UpdateContentObject,)
    serializer_class = ContentSerializer
    lookup_field = 'id'
    def get_queryset(self,*args,**kwargs):
        id=self.kwargs['id']
        query=Content.objects.filter(id=id).all()
        return query
    def get(self, request, *args, **kwargs):
        return self.retrieve(request,*args,**kwargs)
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)


# Create your views here.
