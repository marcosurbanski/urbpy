import pytest
from django.urls import reverse
from model_bakery import baker
from pypro.django_assertions import assert_contains

@pytest.fixture
def usuario_logado(db, django_user_model):
    usuario_modelo = baker.make(django_user_model)    
    return usuario_modelo

@pytest.fixture
def client_com_usuario_logado(usuario_logado, client):
    client.force_login(usuario_logado)
    return client
