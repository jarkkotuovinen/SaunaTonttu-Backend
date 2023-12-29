from rest_framework import serializers

from ...models import GlobalSettings, Page


class GlobalSettingsSerializer(serializers.ModelSerializer):
    logo_url = serializers.CharField(source='get_logo_url', read_only=True)

    class Meta:
        model = GlobalSettings
        fields = "__all__"


class PageSerializer(serializers.ModelSerializer):
    thumbnail_url = serializers.CharField(source='get_thumbnail_url', read_only=True)

    class Meta:
        model = Page
        fields = "__all__"
