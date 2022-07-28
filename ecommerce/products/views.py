from django.shortcuts import render
from products.models import products
from rest_framework.views import APIView
from rest_framework.response import Response

class Productview(APIView):
    def get(self,request,*args,**kwargs):
        if "price" in request.query_params:
            price=int(request.query_params.get("price"))
            price_lt_five=[product for product in products if product["price"]<=price]
            return Response(data=price_lt_five)
        if "limit" in request.query_params:
            limit=int(request.query_params.get("limit"))
            prod=[product for product in products if product["id"]<=limit]
            return Response(data=prod)

        return Response(data=products)
    def post(self,request,*args,**kwargs):
        pro_details=request.data
        return Response(data=pro_details)


# Create your views here.
