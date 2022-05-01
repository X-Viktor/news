from rest_framework import serializers

from news.models import Type, News


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['name', 'color']


class NewsSerializer(serializers.ModelSerializer):
    type_color = serializers.CharField(source='type.color', read_only=True)
    type_name = serializers.CharField(source='type.name', read_only=True)

    class Meta:
        model = News
        fields = [
            'name', 'short_desc', 'type_name',
            'type_color', 'description', 'type',
        ]
        extra_kwargs = {
            'type': {'write_only': True},
            'description': {'write_only': True},
        }


class NewsDetailSerializer(serializers.ModelSerializer):
    type_name = serializers.CharField(source='type.name', read_only=True)

    class Meta:
        model = News
        fields = '__all__'
        extra_kwargs = {
            'type': {'write_only': True}
        }
