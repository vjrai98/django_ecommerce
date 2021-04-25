from rest_framework import authentication
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend


class EmailBackend():
    """
    backend to use email as a login method
    """
    def authenticate(self,request,username=None,password=None,**kwargs):
        "check if user exists and password is correct"
        User = get_user_model()
        try:
            print(username)
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None
    
    def get_user(self,user_id):
        print("get user called")
        User = get_user_model()
        try:
            return User.objects.get(pk=user_id)
        except:
            return None


class DrfAuthBackend(authentication.BaseAuthentication):

    def authenticate(self, email=None, password=None):
        User = get_user_model()
        print("authenticate called")
        try:
            user = get_user_model().objects.get(email=email)
            if user.check_password(password):
                return user,None
        except User.DoesNotExist:
                return None
