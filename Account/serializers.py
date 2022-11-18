from django.contrib.auth.models import User

from .models import AccountUser
from rest_framework import serializers
from .models import AccountUser

class Register_Account(serializers.Serializer):
    Country=[('Canada','Canada'),
             ('USA','USA'),
             ('Iran','Iran')]
    country=serializers.MultipleChoiceField(choices=Country)
    username = serializers.CharField()
    firstname = serializers.CharField()
    password = serializers.CharField()
    repassword=serializers.CharField()
    image = serializers.ImageField(required=False,allow_null=True,allow_empty_file=True)
    phone = serializers.CharField(required=False,allow_null=True,allow_blank=True)
    email=serializers.CharField()
    def validate(self, data):
        password=data.get('password')
        repassword=data.get('repassword')
        if repassword!=password:
            raise serializers.ValidationError("Passwords are not match.Please Try Again")
        return data

    def validate_username(self,value):
        selected_username=User.objects.filter(username=value)
        if selected_username:
            raise serializers.ValidationError("Choose Another Username")
        return value
    def validate_email(self,value):

        selected_email=User.objects.filter(email=value)
        if selected_email:

            raise serializers.ValidationError("Choose Another Email")
        return value
    def create(self, validated_data):
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
        fields=['useraccount','image','country','phone']
