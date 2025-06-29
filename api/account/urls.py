from django.urls import path
from account.views import RegisterView
from account.views import LoginView
from account.views import SettingsView, ChangePasswordView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("settings/", SettingsView.as_view(), name="user_settings"),
    path("change-password/", ChangePasswordView.as_view(), name="change_password"),
]