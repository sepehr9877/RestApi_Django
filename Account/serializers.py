from django.contrib.auth.models import User

from .models import AccountUser
from rest_framework import serializers
from .models import AccountUser

class Register_Account(serializers.Serializer):
    Country=[('1','Canda'),
             ('2','USA'),
             ('3','Iran')]
    country=serializers.MultipleChoiceField(choices=Country)
    username = serializers.CharField()
    firstname = serializers.CharField()
    password = serializers.CharField()
    repassword=serializers.CharField()
    image = serializers.ImageField()
    phone = serializers.CharField()
    def validate_password(self,values):
        return values
    def validate_repassword(self,value,data):
        if value!=data.get:
            raise serializers.ValidationError('Passwords Are not Match')
        else:
            return value
    def validate_username(self,value):
        selected_username=User.objects.filter(username=value)
        if selected_username:
            raise serializers.ValidationError("Choose Another Username")
        else:
            return value

    def create(self, validated_data):

        username=self.validated_data['username']
        firstname=self.validated_data['firstname']
        password=self.validated_data['password']
        image=self.validated_data['image']
        country=self.validated_data['country']
        phone=self.validated_data['phone']
        print(phone)
        # created_user=User.objects.create_user(username=username,
        #                                       password=password,
        #                                       firstname=firstname)
        # created_account=AccountUser.objects.create(useraccount_id=created_user.id,
        #                                            image=image,
        #                                            country=country,
        #                                            phone=phone,
        #                                               )
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model=AccountUser
        fields=['useraccount','image','country','phone']
