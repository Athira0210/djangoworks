from django.shortcuts import render
from menus.models import menu_items
from rest_framework.views import APIView
from rest_framework.response import Response

class Itemview(APIView):
    def get(self,request,*args,**kwargs):
        print(request.query_params)
        if "category" in request.query_params:
            items=request.query_params.get("category")
            data=[item for item in menu_items if item["category"]==items]
            return Response(data=data)

        if "rating" in request.query_params:
            rating=int(request.query_params.get("rating"))
            data=[item for item in menu_items if item["rating"]<=rating]
            return Response(data=data)
        return Response(data=menu_items)

    def post(self,request,*args,**kwargs):
        data=request.data
        menu_items.append(data)
        return Response(data=data)

class Itemdetailview(APIView):
    def get(self,request,*args,**kwargs):
        icode=kwargs.get("icode")
        dish=[item for item in menu_items if item["code"]==icode].pop()
        return Response(data=dish)
    def put(self,request,*args,**kwargs):
        icode=kwargs.get("icode")
        dish=[item for item in menu_items if item["code"]==icode].pop()
        dish.update(request.data)
        return Response(data=dish)

# Create your views here.
