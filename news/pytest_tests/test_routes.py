import pytest
from http import HTTPStatus

from django.urls import reverse
from pytest_django.asserts import assertRedirects



def test_with_client(db, client):
    response = client.get('/')
    assert response.status_code == 200

def test_detail_page(db, client, news):
    url = reverse('news:detail', args=(news.id,))
    response = client.get(url)
    assert response.status_code == HTTPStatus.OK


@pytest.mark.parametrize(
        'page, key',
        (
            ('news:home', None),
            ('news:detail', pytest.lazy_fixture('news')),
            ('users:login', None),
            ('users:logout', None),
            ('users:signup', None),
        )
)