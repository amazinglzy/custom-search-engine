from datetime import datetime
from rest_framework import serializers
from .docs import Page


class PageSerializer(serializers.Serializer):
    id = serializers.UUIDField(source='meta.id', required=False)
    url = serializers.CharField()
    title = serializers.CharField()
    content = serializers.CharField()

    def create(self, validated_data):
        instance = Page(**validated_data)
        instance.refreshed_at = datetime.now()
        instance.save()
        return instance

    def update(self, instance, validated_data, partial=False):
        instance.url = validated_data.get('url', instance.url if partial else None)
        instance.title = validated_data.get('title', instance.title if partial else None)
        instance.content = validated_data.get('content', instance.content if partial else None)
        instance.refreshed_at = datetime.now()
        instance.save()
        return instance
