from rest_framework import serializers
from productapi.models import Products

class Productserializer(serializers.Serializer):
    id=serializers.CharField(read_only=True)
    name=serializers.CharField()
    category=serializers.CharField()
    price=serializers.IntegerField()
    rating=serializers.FloatField()

    def validate(self,data):
        price=data.get("price")
        if price<0:
            raise serializers.ValidationError("invalid price")

        return data

class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields='__all__'