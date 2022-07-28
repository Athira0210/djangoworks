from django.shortcuts import render
from django.shortcuts import render

from blogapi.models import posts
from rest_framework.views import APIView
from rest_framework.response import Response

class Postview(APIView):
    def get(self,request,*args,**kwargs):
        if "liked_by" in request.query_params:
            id=int(request.query_params.get("liked_by"))
            data=[post for post in posts if id in post.get("liked_by")]
            return Response(data=data)
        return Response(data=posts)
    def post(self,request,*args,**kwargs):
        data=request.data
        return Response(data=data)
class Postdetaolview(APIView):
    def get(self,request,*args,**kwargs):
        pid=kwargs.get("pid")
        post=[post for post in posts if post["postId"]==pid].pop()
        return Response(data=post)

# Create your views here.
