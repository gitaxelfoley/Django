from rest_framework import serializers
from .models import Shoe

class ShoeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shoe
        fields = ('id', 'brand', 'type', 'price', 'size', 'description', 'height_field', 'width_field')


