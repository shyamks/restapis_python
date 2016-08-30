from rest_framework import serializers
import models


class ReporterSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    pub_date = serializers.DateField(required=False)
    dat = serializers.DateField(allow_null=True, required=False)
    headline = serializers.CharField(max_length=200, required=False)
    content = serializers.CharField(required=False)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return models.Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.pub_date = validated_data.get('pub_date')
        instance.dat = validated_data.get('dat')
        instance.headline = validated_data.get('headline')
        instance.content = validated_data.get('content')
        instance.save()
        return instance