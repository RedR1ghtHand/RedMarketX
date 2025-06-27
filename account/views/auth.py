from rest_framework_simplejwt.views import TokenObtainPairView
from account.serializers import LoginSerializer


class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer
