import json

from django.shortcuts import render

# Create your views here.
from rest_framework import mixins
from rest_framework.generics import ListAPIView
from Account.models import AccountUser
from .serializers import AccountSerializer,Register_Account
from .permissions import AccountPermission
from rest_framework import permissions
class SuperAccount(ListAPIView):
    serializer_class = AccountSerializer
    queryset = None
    permission_classes=(permissions.IsAdminUser,)
    def get_queryset(self):
        self.queryset=AccountUser.objects.all()
        return self.queryset
class AccountUserList(SuperAccount,
                      mixins.ListModelMixin):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def get(self, request, *args, **kwargs):
        print("get")
        return self.list(request,*args,**kwargs)
class RegisterAccount(SuperAccount,
                      mixins.CreateModelMixin):
    permission_classes=(permissions.AllowAny,)
    serializer_class =Register_Account
    queryset = None
    def get_queryset(self):None
    def post(self,request,*args,**kwargs):
        serializer=Register_Account(data=self.request.data or self.request.FILES)
        print(self.request.FILES['image'])
        data=self.request.data
        if data:
            self.serializer_class.validate_email(Register_Account(),value=data['email'])
            self.serializer_class.validate(Register_Account(),data=data)
            self.serializer_class.validate_username(Register_Account(),value=data['username'])
            if serializer.is_valid():
                print("enter valid")
                self.serializer_class.create(self=Register_Account(data=data),validated_data=data)
        return self.create(request,*args,**kwargs)
