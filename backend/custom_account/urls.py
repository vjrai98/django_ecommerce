from django.contrib import admin
from django.urls import path,include
from .views import CreateAccount,GetUsers,GetUserDetails
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', CreateAccount.as_view(), name='register'),
    path('users/', GetUsers.as_view(), name='users'),
    path('login/', obtain_auth_token, name='login'),
    path('user/<int:pk>', GetUserDetails.as_view(), name='user_details'),
    

]
