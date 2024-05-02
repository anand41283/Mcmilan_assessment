from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from app.models import *
from app.serializer import *
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import login,authenticate,logout
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class UserRegistrationView(APIView):
    serializer_class=Userregistration
    def post(self, request):
        serializer=Userregistration(data=request.data)
        if serializer.is_valid():
            user = User.objects.create_superuser(
                username=serializer.validated_data['username'],
                email=serializer.validated_data['email'],
                password=serializer.validated_data['password']
            )
            return Response({'message': 'Admin registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class LoginView(APIView):
#     serializer_class=Login
#     def post(self,request):
#         serializer=Login(data=request.data)
#         if serializer.is_valid():
#             U_name=serializer.validated_data['username']
#             pswd=serializer.validated_data['password']
#             user=authenticate(username=U_name,password=pswd)
#             if user and user.is_superuser:
#                 login(request, user)
#                 return Response({'message': 'Admin logged in successfully'}, status=status.HTTP_200_OK)
#             else:
#                 return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)
    
class Adddept(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        serializer=Deptserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Add successfully'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class StudentView(ViewSet):

    permission_classes=[IsAuthenticated]

    def create(self,request,*args,**kwargs):
        serializers=Studentserializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'message': 'Add successfully'}, status=status.HTTP_200_OK)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def list(self,request,*args,**kwargs):
        qs=Student.objects.all()
        serializers=Studentserializer(qs,many=True)
        return Response(data=serializers.data)
    
    def update(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Student.objects.get(id=id)
        serializers=Studentserializer(data=request.data,instance=qs)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Student.objects.get(id=id)
        serializers=Studentserializer(qs)
        return Response(serializers.data)
    
    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Student.objects.get(id=id).delete()
        return Response({'message': 'delete successfully'}, status=status.HTTP_200_OK)