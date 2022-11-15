from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Products
class ProductSerializer(serializers.Serializer):
    owner=serializers.ReadOnlyField(source='owner.username')
    id=serializers.IntegerField()
    title=serializers.CharField()
    image=serializers.ImageField()

    def create(self, validated_data):
        return Products.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.title=validated_data.get('title',instance.title)
        instance.image=validated_data.get('image',instance.image)
        instance.save()
        return instance
class ProductuserSerializer(serializers.ModelSerializer):
    owner=serializers.PrimaryKeyRelatedField(many=True,queryset=Products.objects.all())
    class Meta:
        model=User
        fields=['id','username','owner']

