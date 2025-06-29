import pytest
from rest_framework import status


@pytest.mark.django_db
def test_user_login(api_client, create_user):
    user = create_user()

    response = api_client.post('/api/account/login/', {"email": user.email, "password": "PassWORD123!"})

    assert response.status_code == status.HTTP_200_OK
    assert 'access' in response.data
    assert 'refresh' in response.data
