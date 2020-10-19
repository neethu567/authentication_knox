from rest_framework import generics

from .models import laptop, employee, company
from .serializers import laptopSerializer, employeeSerializer, companySerializer
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer
from django.contrib.auth import login

from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

class laptopList(generics.ListCreateAPIView):
    queryset = laptop.objects.all()
    serializer_class = laptopSerializer


class LaptopDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = laptop.objects.all()
    serializer_class = laptopSerializer


class employeeList(generics.ListCreateAPIView):
    queryset = employee.objects.all()
    serializer_class = employeeSerializer


class employeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = employee.objects.all()
    serializer_class = employeeSerializer


class companyList(generics.ListCreateAPIView):
    queryset = company.objects.all()
    serializer_class = companySerializer


class companyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = company.objects.all()
    serializer_class = companySerializer

from rest_framework.views import APIView
# from .serializers import loginserializer
from django.contrib.auth import login as django_login, authenticate


# class loginview(APIView):
#    def post(self,request):
#        serializer=loginserializer(data=request.data)
#        serializer.is_valid(raise_exception=True)
#        user=serializer.validated_data['user']
#        django_login(request,user)
#        token, created=Token.objects.get_or_create(user=user)
#        return Response({'token':token.key},status=200)
#
# class logoutview(APIView):
#     pass

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)