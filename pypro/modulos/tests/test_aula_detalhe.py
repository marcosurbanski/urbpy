import pytest
from django.urls import reverse
from model_bakery import baker

from pypro.django_assertions import assert_contains
from pypro.modulos.models import Aula, Modulo


@pytest.fixture
def modulo(db):
    return baker.make(Modulo)


@pytest.fixture
def aula(modulo):
    return baker.make(Aula, modulo=modulo)


@pytest.fixture
def resp(client, aula):
    resp = client.get(reverse('modulos:aula', kwargs={'slug': aula.slug}))
    return resp


def test_titulos(resp, aula: Aula):
    assert_contains(resp, aula.titulo)


def test_video_id(resp, aula: Aula):
    assert_contains(resp, f'src="https://www.youtube.com/embed/{ aula.video_id }"')
