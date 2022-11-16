from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Products
class ProductSerializer(serializers.Serializer):
    owner=serializers.ReadOnlyField(source='owner.username')
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
    class Meta:
        model=Products
        fields=[
            'owner',
            'title',
            'image'
        ]
    

