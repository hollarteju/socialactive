from django.shortcuts import render
from rest_framework  import viewsets, status
from .models import *
from .serializer import *
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.


@api_view(["POST"])
def register_user(request):
    if request.method == "POST":
        serializer = UserDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"successful"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({"message":"Hello worondh"})


