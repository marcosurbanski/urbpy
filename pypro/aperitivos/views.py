from django.shortcuts import render
from django.urls import reverse


"""
    Classe video: representa um video com os atributos especificos

    slug: Indentificador curto do video (uma chave unica)
    titulo: Titulo do video usado na interface
    synthesia_id: ID do video gerado na plataforma Synthesia

    Videos: cria uma lista de objetos da classe Video, cada um representa um video especifico

    videos_dct: cria um dicionario onde a chave é o 'slug' do video e o valor é o objeto Video correspondente
    Isso permite acessar rapidamente um video especifico pelo seu slug.

    Função indice: View que renderiza a página inicial com a lista de videos disponiveis.
    função video: view que renderiza uma página para um video especifico, com base no slug da URL.
"""


class Video:
    def __init__(self, slug, titulo, synthesia_id):
        self.slug = slug
        self.titulo = titulo
        self.synthesia_id = synthesia_id

    def get_absolute_url(self):
        return reverse('aperitivos:video', args=(self.slug,))


videos = [
    Video('motivacao', 'Video Aperitivo: Motivação', '445f84c2-eb92-49da-a4dc-b4c0ec772fed'),
    Video('show', 'Video Aperitivo: Apresentação', '8f1bdd22-99a8-4ca5-b615-a90929485bf1')
]

videos_dct = {v.slug: v for v in videos}


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})


def video(request, slug):
    video = videos_dct[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
