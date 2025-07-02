import pytest
from django.urls import reverse
from pypro.django_assertions import assert_contains
from model_bakery import baker
from pypro.aperitivos.models import Video

"""
Testes da view 'indice' do app 'aperitivos'.

Função resp:
    - Fixture do pytest que simula uma requisição GET para a view 'indice'.
    - Retorna a resposta HTTP (HttpResponse), que será utilizada nos testes.
    - Permite reaproveitamento da resposta em diferentes testes sem repetir código.

Função test_status_code:
    - Verifica se a resposta da requisição tem status 200 (sucesso).
    - Garante que a página está acessível e não retorna erro.

Função test_titulo_video:
    - Testa se os títulos esperados dos vídeos estão presentes no HTML da página.
    - Usa @pytest.mark.parametrize para testar automaticamente diferentes valores de título.
    - Cada item da lista será testado como se fosse um teste separado.

Função test_link_video:
    - Testa se os links para as páginas de cada vídeo estão corretamente renderizados na página.
    - Usa @pytest.mark.parametrize com os slugs dos vídeos.
    - Para cada slug, gera a URL correspondente com reverse() e verifica se ela está presente no HTML.

Uso do @pytest.mark.parametrize:
    - Permite passar múltiplos valores para o mesmo teste.
    - Cria dinamicamente vários testes com base em uma lista de entradas.
    - Melhora a cobertura dos testes com menos repetição de código.
"""


# o modelo comentado foi para realizar apenas 1 texto especifico foi implementado a bibliotexa model_mommy para testes aleatorios.
@pytest.fixture
def videos(db):
    # v = Video(slug='motivacao', titulo='Video Aperitivo: Motivação', synthesia_id='445f84c2-eb92-49da-a4dc-b4c0ec772fed')
    # v.save()
    # return v
    return baker.make(Video, 3)


@pytest.fixture
def resp(client, videos):
    return client.get(reverse('aperitivos:indice'))


def test_status_code(resp):
    assert resp.status_code == 200


def test_titulo_video(resp, videos):
    for video in videos:
        assert_contains(resp, video.titulo)


def test_link_video(resp, videos):
    for video in videos:
        video_link = reverse('aperitivos:video', args=(video.slug, ))
        assert_contains(resp, f'href="{video_link}"')
