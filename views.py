from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from productapi.models import Products,Reviews
from productapi.serializers import Productserializer
from rest_framework import status
from productapi.serializers import ProductModelSerializer,UserSerializer,ReviewSerializer
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework import authentication,permissions
from rest_framework.decorators import action



class Productsview(APIView):
    def get(self,request,*args,**kwargs):
        qs=Products.objects.all()
        serializer=Productserializer(qs,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    def post(self,request,*args,**kwargs):
        serializer=Productserializer(data=request.data)
        if serializer.is_valid():
            Products.objects.create(**serializer.validated_data,status=status.HTTP_201_CREATED)
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ProductDetailView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Products.objects.get(id=id)
        serializer=Productserializer(qs)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        instance=Products.objects.filter(id=id)
        serializer=Productserializer(data=request.data)
        if serializer.is_valid():
            instance.name=serializer.validated_data.get("name")
            instance.category=serializer.validated_data.get("category")
            instance.price=serializer.validated_data.get("price")
            instance.rating=serializer.validated_data.get("rating")

            #instance.save()
            instance.update(**serializer.validated_data)
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,*args,**kwargs):
        id=kwargs.get("id")

        instance=Products.objects.get(id=id)
        serializer=Productserializer(instance)
        instance.delete()

        return Response({"msg":"deleted"},status=status.HTTP_400_BAD_REQUEST)

class ProductModelView(APIView):
    def get(self,request,*args,**kwargs):
        qs=Products.objects.all()
        if "category" in request.query_params:
            qs=qs.filter(category__contains=request.query_params.get("category"))
        if "price_gt" in request.query_params:
            qs=qs.filter(price__gte=request.query_params.get("price_gt"))
        serializer=ProductModelSerializer(qs,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    def post(self,request,*args,**kwargs):
        serializer=ProductModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductdetailModelview(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Products.objects.get(id=id)
        serializer=ProductModelSerializer(qs)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        object=Products.objects.all(id=id)
        serializer=ProductModelSerializer(data=request.data,instance=object)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        id = kwargs.get("id")
        instance = Products.objects.get(id=id)
        instance.delete()

        return Response({"msg": "deleted"}, status=status.HTTP_400_BAD_REQUEST)

class ProductViewsetview(ViewSet):
    def list(self,request,*args,**kwargs):
        qs=Products.objects.all()
        serializer=ProductModelSerializer(qs,many=True)
        return Response(data=serializer.data)

    def create(self,request,*args,**kwargs):
        serializer=ProductModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Products.objects.get(id=id)
        serializer=ProductModelSerializer(qs)
        return Response(data=serializer.data)

    def update(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        object=Products.objects.get(id=id)
        serializer=Productserializer(instance=object,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def destroy(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        instance = Products.objects.get(id=id)
        instance.delete()

        return Response({"msg": "deleted"}, status=status.HTTP_400_BAD_REQUEST)


class ProductModelViewsetView(ModelViewSet):
    serializer_class = ProductModelSerializer
    queryset = Products.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permissions=[permissions.IsAuthenticated]

    @action(methods=['get'],detail=True)
    def get_reviews(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        product=Products.objects.get(id=id)
        review=product.reviews_set.all()
        serializer=ReviewSerializer(review,many=True)
        return Response(data=serializer.data)

    @action(methods=["post"],detail=True)
    def post_review(self,request,*args,**kwargs):
        author=request.user
        id = kwargs.get("pk")
        product = Products.objects.get(id=id)
        serializer=ReviewSerializer(data=request.data,context={"author":author,"product":product})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

        # @action(methods=["post"], detail=True)
        # def post_review(self, request, *args, **kwargs):
        #     author = request.user
        #     id = kwargs.get("pk")
        #     product = Products.objects.get(id=id)
        # review=request.data.get("review")
        # rating=request.data.get("rating")
        # qs=Reviews.objects.create(
        #     author=author,
        #     product=product,
        #     rating=rating,
        #     review=review
        # )
        # serializer=ReviewSerializer(qs)
        # return Response(data=serializer.data)


from django.contrib.auth.models import User

class UserModelViewsetView(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
