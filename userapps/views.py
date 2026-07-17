from rest_framework import status, serializers
from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

from .serializers import RegistrationSerializer
from . models import Profile

# function class to register
class RegistrationView(APIView):
    def post(self,request):
        try:
            serializers = RegistrationSerializer(data=request.data)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data, status=status.HTTP_201_CREATED)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# function class to LOGIN
class LoginView(APIView):
    def post(self,request):
        try:
            username= request.data.get('username')
            password= request.data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return Response({"Message":f"{user.username} logged in successfully"}, status=status.HTTP_200_OK)
            return Response({"Message":f"Invalid credential"}, status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            return Response({"error":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# function class to LOGOUT
class LoginOutView(APIView):
    def post(self,request):
        try:
            logout(request)
            return Response({"Message":"User logged out successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)