from rest_framework import serializers
from productapi.models import Products,Reviews
from django.contrib.auth.models import User

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

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=[
            "first_name",
            "last_name",
            "username",
            "email",
            "password"
        ]

    def create(self, validated_data):

        return User.objects.create_user(**validated_data)

class ReviewSerializer(serializers.ModelSerializer):
    author=serializers.CharField(read_only=True)
    product=serializers.CharField(read_only=True)
    class Meta:
        model=Reviews
        fields="__all__"

    def create(self, validated_data):
        author=self.context.get("author")
        product=self.context.get("product")
        return Reviews.objects.create(**validated_data,author=author,product=product)

