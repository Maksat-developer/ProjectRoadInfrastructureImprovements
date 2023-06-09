from django.shortcuts import render

# Create your views here.
from .serializers import MessageModelSerializer
from rest_framework import generics
from .models import MessageModel



class MessageModelListCreate(generics.ListCreateAPIView):
    queryset = MessageModel.objects.all()
    serializer_class = MessageModelSerializer



class MessageModelDelete(generics.RetrieveDestroyAPIView):
    queryset = MessageModel.objects.all()
    serializer_class = MessageModelSerializer



class MessageModelUpdate(generics.RetrieveUpdateAPIView):
    queryset = MessageModel.objects.all()
    serializer_class = MessageModelSerializer



