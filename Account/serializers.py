from .models import AccountUser
from rest_framework import serializers
from .models import AccountUser
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model=AccountUser
        fields=['useraccount','image','country','phone']