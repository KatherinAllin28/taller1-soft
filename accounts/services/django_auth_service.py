from django.contrib.auth import authenticate as django_auth
from .auth_interface import IAuthService

class DjangoAuthService(IAuthService):
    def authenticate(self, request, username: str, password: str):
        return django_auth(request, username=username, password=password)
