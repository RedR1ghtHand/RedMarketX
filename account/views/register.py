from rest_framework.generics import CreateAPIView
from account.serializers.register import RegisterSerializer
from account.models import User


class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()
