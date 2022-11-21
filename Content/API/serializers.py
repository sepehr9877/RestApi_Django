from rest_framework import serializers
from Content.models import Content
class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Content
        fields=['user_content','content','created_date']