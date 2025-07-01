import pytest
from django.urls import reverse
from pypro.django_assertions import assert_contains

"""
Testes da view 'video' do app 'aperitivos'.

Função resp (fixture):
    - Realiza uma requisição GET para a view 'video' passando o slug 'motivacao'.
    - Retorna a resposta HTTP (HttpResponse) para ser reutilizada nos testes.
    - Facilita a repetição de testes sem chamar a view manualmente a cada vez.

Função test_status_code:
    - Verifica se a resposta da requisição possui status HTTP 200 (OK).
    - Garante que a página do vídeo está acessível e não retorna erro.

Função test_titulo_video:
    - Verifica se o título renderizado na página corresponde ao esperado.
    - Usa assert_contains (customizado com BeautifulSoup) para validar o conteúdo HTML.
    - Título esperado: <h1 class="mt-4 mb-3">Video Aperitivo: Motivação</h1>

Função test_conteudo_video:
    - Verifica se o iframe com o link do vídeo (via Synthesia) está presente na página.
    - Garante que o conteúdo principal da view está carregando corretamente.
"""


@pytest.fixture
def resp(client, db):
    return client.get(reverse('aperitivos:video', args=('motivacao',)))


def test_status_code(resp):
    assert resp.status_code == 200


def test_titulo_video(resp):
    assert_contains(resp, '<h1 class="mt-4 mb-3">Video Aperitivo: Motivação</h1>')


def test_conteudo_video(resp):
    assert_contains(resp, '<iframe src="https://share.synthesia.io/embeds/videos/445f84c2-eb92-49da-a4dc-b4c0ec772fed"')
