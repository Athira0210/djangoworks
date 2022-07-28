from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime

class Goodmorning(APIView):
    def get(self,request,*args,**kwargs):
        return Response({"message":"goodmorning"})

class Goodafternoon(APIView):
    def get(self,request,*args,**kwargs):
        return Response({"message":"goodafternoon"})

class Greetingsview(APIView):
    def get(self,request,*args,**kwargs):
        cur_date=datetime.now()
        cur_hour=cur_date.hour
        greetings = ""
        if cur_hour < 12:
            greetings="good morning"
        elif cur_hour < 18:
            greetings="good afternoon"
        return Response({"message":greetings})



# Create your views here.
