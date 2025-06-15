from django.test import Client
from django.urls import reverse
from pypro.django_assertions import assert_contains
import pytest

@pytest.fixture
def resp(client):
    resp = client.get(reverse('home'))
    return resp

def test_status_code(resp):   
    assert resp.status_code == 200

def test_title(resp):    
    assert_contains(resp, '<title>UrbPy - Future IT course platform</title>')

def test_home_link(resp):    
    assert_contains(resp, 'content="Marcos Urbanski"')


def test_description(resp):   
    assert_contains(resp, 'content="Pagina da aplicação URBPY"')

def test_author(resp):   
    assert_contains(resp, 'href="/">UrbPy</a>')

