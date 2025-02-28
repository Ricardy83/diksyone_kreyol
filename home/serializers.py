from rest_framework import serializers
from .models import Mot, Synonyme, Antonyme, Expression

class MotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mot
        fields = '__all__'

class SynonymeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Synonyme
        fields = '__all__'

class AntonymeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Antonyme
        fields = '__all__'

class ExpressionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expression
        fields = '__all__'
