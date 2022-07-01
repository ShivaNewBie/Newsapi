from rest_framework import serializers

from news.models import Article

class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.CharField()
    description = serializers.CharField()
    body = serializers.CharField()
    location = serializers.CharField()
    publication_date = serializers.DateField()
    active = serializers.BooleanField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def create(self,validated_data):
        pass 
    def update(self,instance,validated_data):
        pass 