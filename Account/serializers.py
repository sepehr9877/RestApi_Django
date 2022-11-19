
from django.contrib.auth.models import User

from .models import AccountUser
from rest_framework import serializers
from .models import AccountUser

class Register_Account(serializers.Serializer):
    country=serializers.CharField()
    username = serializers.CharField()
    firstname = serializers.CharField()
    password = serializers.CharField()
    repassword=serializers.CharField()
    image = serializers.ImageField(required=False,allow_null=True,allow_empty_file=True,default=None)
    phone = serializers.CharField(required=False,allow_null=True,allow_blank=True,default=None)
    email=serializers.CharField()
    def validate(self, data):
        password=data.get('password')
        repassword=data.get('repassword')
        if repassword!=password:
            raise serializers.ValidationError("Passwords are not match.Please Try Again")
        return data

    def validate_username(self,value):
        print("check username")
        selected_username=User.objects.filter(username=value)
        if selected_username:
            raise serializers.ValidationError("Choose Another Username")
        return value
    def validate_email(self,value):
        print("check email")
        selected_email=User.objects.filter(email=value)
        if selected_email:

            raise serializers.ValidationError("Choose Another Email")
        return value
    def create(self, validated_data):
        if self.is_valid():
            print(validated_data)
            username=self.validated_data['username']
            firstname=self.validated_data['firstname']
            password=self.validated_data['password']
            image=self.validated_data['image']
            country=self.validated_data['country']
            phone=self.validated_data['phone']
            email=self.validated_data['email']
            print(username)
            created_user=User.objects.create_user(username=username,
                                                  password=password)
            User.objects.filter(id=created_user.id).update(first_name=firstname,email=email)
            created_account=AccountUser.objects.create(useraccount_id=created_user.id,
                                                       image=image,
                                                       country=country,
                                                       phone=phone,
                                                          )
            return created_account

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model=AccountUser
        fields=['id','image','country','phone','useraccount']
class UserDetail(serializers.ModelSerializer):
    UserDetailSpec=AccountSerializer(read_only=True,many=True)
    class Meta:
        model=User
        fields=['id','username','email','password','UserDetailSpec']
class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()
    def validate(self,data):
        username=data.get('username')
        password=data.get('password')
        selected_user=User.objects.filter(username=username)
        print(selected_user)
        if not selected_user:
            raise serializers.ValidationError("Wrong Username or Password")
        else:
            return username,password
    def create(self, validated_data):
        print("Create")
        pass
