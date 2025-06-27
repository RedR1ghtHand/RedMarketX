import pytest
from account.models import User
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user_payload():
    return {
        "email": "test@example.com",
        "mc_username": "TestUser",
        "password": "PassWORD123!",
    }


@pytest.fixture
def create_user(user_payload):
    def _create_user(**overrides):
        data = user_payload.copy()
        data.update(overrides)
        return User.objects.create_user(**data)
    return _create_user


@pytest.fixture
def auth_client(create_user, api_client, user_payload):
    user = create_user()
    res = api_client.post("/api/account/login/", {"email": user.email, "password": user_payload['password']})
    token = res.data["access"]
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
    return api_client
