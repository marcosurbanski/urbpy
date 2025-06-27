import pytest
from django.urls import reverse
from pypro.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('aperitivos:indice'))


def test_status_code(resp):
    assert resp.status_code == 200


@pytest.mark.parametrize(
        'titulo',
        [
            'Video Aperitivo: Motivação',
            'Video Aperitivo: Apresentação'
        ]
)
def test_titulo_video(resp, titulo):
    assert_contains(resp, titulo)

"""
def test_conteudo_video(resp):
    assert_contains(resp, '<iframe src="https://share.synthesia.io/embeds/videos/445f84c2-eb92-49da-a4dc-b4c0ec772fed"')
"""