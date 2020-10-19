from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .import views
from knox import views as knox_views
from .views import LoginAPI
from django.urls import path
from .views import RegisterAPI
from django.urls import path


urlpatterns = [
    path('laptoplist/', views.laptopList.as_view()),
    path('laptopdetail/<int:pk>/', views.LaptopDetail.as_view()),
    path('employeelist/', views.employeeList.as_view()),
    path('employeedetail/<int:pk>/', views.employeeDetail.as_view()),
    path('companylist/', views.companyList.as_view()),
    path('companydetail/<int:pk>/', views.companyDetail.as_view()),
    path('registerview/',  RegisterAPI.as_view()),
    # path('logoutview/', knox_views.LogoutView.as_view()),
    path('loginview/',  LoginAPI.as_view()),
    # path('logoutall/', knox_views.LogoutAllView.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)