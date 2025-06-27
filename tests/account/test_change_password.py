import pytest
from rest_framework import status


@pytest.mark.django_db
def test_change_password_and_login(auth_client, api_client, user_payload):
    response = auth_client.post("/api/account/change-password/", {
        "old_password": user_payload["password"],
        "new_password": "NewSecurePassWORD123!"
    })

    assert response.status_code == status.HTTP_200_OK

    response = api_client.post('/api/account/login/', {
        "email": user_payload["email"],
        "password": "NewSecurePassWORD123!"
    })
    assert response.status_code == status.HTTP_200_OK
    assert "access" in response.data
