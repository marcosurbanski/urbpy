import pytest
from model_bakery import baker
from django.urls import reverse
from pypro.aperitivos.models import Video
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


# o modelo comentado foi para realizar apenas 1 texto especifico foi implementado a bibliotexa model_mommy para testes aleatorios.
@pytest.fixture
def video(db):
    # v = Video(slug='motivacao', titulo='Video Aperitivo: Motivação', synthesia_id='445f84c2-eb92-49da-a4dc-b4c0ec772fed')
    # v.save()
    # return v
    return baker.make(Video)


@pytest.fixture
def resp(client, video):
    return client.get(reverse('aperitivos:video', args=(video.slug,)))


@pytest.fixture
def resp_video_nao_encontrado(client, video):
    return client.get(reverse('aperitivos:video', args=(video.slug+'video_nao_existente',)))


def test_status_code_video_nao_encontrado(resp_video_nao_encontrado):
    assert resp_video_nao_encontrado.status_code == 404


def test_status_code(resp):
    assert resp.status_code == 200


def test_titulo_video(resp, video):
    assert_contains(resp, video.titulo)


def test_conteudo_video(resp, video):
    assert_contains(resp, f'<iframe src="https://share.synthesia.io/embeds/videos/{video.synthesia_id}"')
