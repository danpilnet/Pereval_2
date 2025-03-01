from rest_framework import serializers


class PerevalSerialzer(serializers.Serializer):
    beauty_title = serializers.CharField(max_length=20)
    title = serializers.CharField(max_length=50)
    other_titles = serializers.CharField(max_length=50)
    connect = serializers.CharField(max_length=254, allow_blank=True)

    # user = ...


class UserSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=254)
