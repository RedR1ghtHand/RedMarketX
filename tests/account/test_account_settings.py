import pytest
from rest_framework import status


@pytest.mark.django_db
def test_change_mc_username(auth_client):
    response = auth_client.patch("/api/account/settings/", {"mc_username": "NewName"})
    assert response.status_code == status.HTTP_200_OK
    assert response.data["mc_username"] == "NewName"
