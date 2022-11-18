from django.shortcuts import render

# Create your views here.
from rest_framework import mixins
from rest_framework.generics import ListAPIView
from Account.models import AccountUser
from .serializers import AccountSerializer
class AccountUserList(ListAPIView,
                      mixins.ListModelMixin):
    serializer_class = AccountSerializer
    queryset = None
    def get_queryset(self):
        self.queryset=AccountUser.objects.all()
        return self.queryset
    def get(self, request, *args, **kwargs):
        return self.list(request,*args,**kwargs)