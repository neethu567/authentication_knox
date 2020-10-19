from .models import laptop, employee, company
from rest_framework import serializers
from django.contrib.auth.models import User


class laptopSerializer(serializers.ModelSerializer):
    class Meta:
        model = laptop
        fields = ['id', 'lap_name']


class employeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = employee
        fields = ['id', 'firstname', 'lastname', 'lap']

class companySerializer(serializers.ModelSerializer):
    class Meta:
        model = company
        fields = ['id', 'company_name', 'emp']

# class loginserializer(serializers.ModelSerializer):
#     class Meta:
#         model=User
#         fields=['id','username','password']
# class loginserializer(serializers.Serializer):
#     username=serializers.CharField()
#     password=serializers.CharField()
#     def validate(self,data):
#         username=data.get('username','')
#         password=data.get('password','')
#
#         if username and password:
#             user=authenticate(username=username,password=password)
#             if user:
#                 if user.is_active:
#                     data['user']=user
#                 else:
#                     msg="user desable"
#                     raise exceptions.validationError(msg)
#
#
#             else:
#                 msg='unable to login'
#                 raise exceptions.validationError(msg)
#         else:
#             msg="must provide username and password"
#             raise exceptions.validationError(msg)
#         return data
# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user