from myapp.models import RecommendModel
from rest_framework import serializers


class RecommendSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RecommendModel
        fields = ("__all__")