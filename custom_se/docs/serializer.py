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


class QueryPageSerializer(serializers.Serializer):
    query = serializers.CharField(default=None)
    page = serializers.IntegerField(default=1)
    page_size = serializers.IntegerField(default=10)

    def create(self, validated_data):
        return validated_data

    def update(self, instance, validated_data):
        return instance


class PageHighlightSerializer(serializers.Serializer):
    url = serializers.SerializerMethodField()
    title = serializers.SerializerMethodField()
    content = serializers.SerializerMethodField()

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    @staticmethod
    def get_highlight_or_origin(field: str, instance: dict):
        highlight = instance.get('highlight', {}).get(field)
        origin = instance['_source'].get(field)
        if highlight:
            return '\n'.join(highlight)
        return origin

    def get_url(self, instance):
        return instance['_source']['url']

    def get_title(self, instance):
        return self.get_highlight_or_origin('title', instance)

    def get_content(self, instance):
        return self.get_highlight_or_origin('content', instance)

