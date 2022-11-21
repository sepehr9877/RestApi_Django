import json

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import mixins
from rest_framework.authtoken.models import Token
from rest_framework.generics import ListAPIView,RetrieveAPIView
from Account.models import AccountUser
from .serializers import AccountSerializer,Register_Account,LoginSerializer,UserDetail
from .permissions import AccountPermission
from rest_framework import permissions
class SuperAccount(ListAPIView):
    serializer_class = AccountSerializer
    queryset = None
    permission_classes=(permissions.IsAdminUser,)
    def get_queryset(self):
        self.queryset=AccountUser.objects.all()
        return self.queryset
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
class LoginPageRequest(SuperAccount
                        ,mixins.CreateModelMixin):
    serializer_class = LoginSerializer
    permission_classes = (AccountPermission,)
    queryset = User.objects.all()
    def get_queryset(self):None
    def post(self,request,*args,**kwargs):
        print("enter")
        print(self.request.data)
        data=self.request.data
        print(data)
        username,password=self.serializer_class.validate(self=LoginSerializer(),data=data)
        print(username)
        print(password)
        authenticated_user=authenticate(self.request,username=username,password=password)
        if authenticated_user:
            print(authenticated_user)
            user_login=login(request=self.request,
                  user=authenticated_user)
            print(user_login)
            print("Response")
            return HttpResponse(self.request.user.id, content_type='text/plain')
        else:
            return HttpResponse("Bad Request", content_type='text/plain')
class GetAccountDetail(SuperAccount,
                       mixins.ListModelMixin):
    permission_classes = (AccountPermission,)
    serializer_class = UserDetail
    user_id=None
    def get_queryset(self):
        queryset = None
        if not self.user_id:
            user_id=self.request.user.id
            if not user_id:

                return None
            if self.request.user.is_superuser:
                queryset=User.objects.all()
            else:
                queryset=User.objects.filter(id=user_id)
        else:
            selected_user=User.objects.filter(id=self.user_id).first()
            if selected_user.is_superuser:
                queryset=User.objects.all()
            else:
                queryset=selected_user
        return queryset
    def get(self, request, *args, **kwargs):
        print("enter to get")
        data=self.request.data
        print("data")
        print(data)
        if data:
            self.user_id=data['id']
            print("get id")
            print(self.user_id)
        return self.list(request,*args,**kwargs)



class UpdateDetail(SuperAccount,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin):
    serializer_class = UserDetail
    lookup_field = 'id'
    permission_classes = (AccountPermission,)
    def get_queryset(self,*args,**kwargs):
        id=self.kwargs['id']

        queryset=User.objects.filter(id=id).all()
        return queryset
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
