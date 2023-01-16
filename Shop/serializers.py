from rest_framework import serializers
from Shop.models import product

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'