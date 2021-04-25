from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.response import Response
from .serializers import RegistrationSerializer,UserSerializer
from rest_framework import permissions
from .models import CustomUser
from rest_framework.exceptions import PermissionDenied
from .permissions import IsAdminUserOrLoggedInUser, IsAdminUser

class CreateAccount(APIView):
   permission_classes = [permissions.AllowAny]

   def post(self, request):
       reg_serializer = RegistrationSerializer(data=request.data)
       if reg_serializer.is_valid():
           new_user = reg_serializer.save()
           if new_user:
              return Response(reg_serializer.data, status=status.HTTP_201_CREATED)
       return Response(reg_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetUsers(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class GetUserDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUserOrLoggedInUser]
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
