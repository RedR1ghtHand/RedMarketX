import pytest
from rest_framework import status


@pytest.mark.django_db
def test_register_user(api_client, user_payload):
    response = api_client.post("/api/account/register/", user_payload)

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data == {
        "email": user_payload["email"],
        "mc_username": user_payload["mc_username"]
    }
