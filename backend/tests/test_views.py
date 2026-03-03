from django.urls import reverse
import pytest

#TODO: test for health  : is vital 200 ok ?
@pytest.mark.django_db
def test_health_check(client):
    url = reverse('health')
    response = client.get(url)
    assert response.status_code == 200

#TODO: test for content : is there a expected contentent in the response ?
    assert response.json() == {
        'status': 'ok',
        'message': 'API is healthy'
    }
#TODO: test for routing : is views correctly routed and showed to urls ?