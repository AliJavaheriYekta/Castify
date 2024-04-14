from django.shortcuts import render
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from user_panel.serializers import UserRegistrationSerializer


# Create your views here.
class UserRegistrationView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        except:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


