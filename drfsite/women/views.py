from ast import Delete
from urllib import response
from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms.models import model_to_dict
from .serializers import WomenSerializer

from .models import Women
# Create your views here.


# class WomenApiView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer

class WomenAPIList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


class WomenAPIUpdate(generics.UpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer 


class WomenApiView(APIView):
    def get(self, request):
        w = Women.objects.all()
        return Response({'posts': WomenSerializer(w, many=True).data})

    
    def post(self, request):
        serializer = WomenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'posts': serializer.data})

    
    def put(self, request, *args, **kwargs):
        pk = request.data.get("pk", None)
        if not pk:
            pk = kwargs.get("pk", None)
            if not pk:
                return Response({"error": "Method Put is not allowed"})

        try:
            instance = Women.objects.get(pk=pk)

        except:
            return Response({"error": "Method Put is not allowed"})

        serializer = WomenSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"Posts": serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method Put is not allowed"})
        try:
            instance = Women.objects.get(pk=pk)
            instance.delete()
        except:
            return Response({"somthing wrong"})

        return Response({"deleted": WomenSerializer(instance).data})
        

