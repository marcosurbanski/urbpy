from django.urls import path
from pypro.aperitivos.views import video, indice

"""
Configuração de URLs do app 'aperitivos'.

- app_name:
    Define um namespace para as URLs do aplicativo. Isso permite referenciar
    as views deste app usando o prefixo 'aperitivos:' em templates e testes.
    Exemplo: reverse('aperitivos:video').

- urlpatterns:
    Lista de rotas (paths) do app.

    path('<slug:slug>', video, name='video'):
        - Rota dinâmica que captura um parâmetro 'slug' da URL.
        - Direciona para a view 'video'.
        - Exemplo de URL: /motivacao → chama a view passando slug='motivacao'.
        - Nome da rota: 'video'.

    path('', indice, name='indice'):
        - Rota raiz do app (ex: /aperitivos/).
        - Direciona para a view 'indice', que geralmente lista os vídeos.
        - Nome da rota: 'indice'.
"""

app_name = 'aperitivos'
urlpatterns = [
    path('<slug:slug>', video, name='video'),
    path('', indice, name='indice'),
]
