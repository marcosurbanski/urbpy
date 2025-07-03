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
from django.shortcuts import render, get_object_or_404
from .models import Video

"""
Para desenvolvimento e testes foi criado os videos abaixo no formato hard coded e adicionar em um dicionario.
videos = [
    Video(slug= 'motivacao', titulo= 'Video Aperitivo: Motivação', synthesia_id= '445f84c2-eb92-49da-a4dc-b4c0ec772fed'),
    Video(slug= 'show', titulo= 'Video Aperitivo: Apresentação', synthesia_id= '8f1bdd22-99a8-4ca5-b615-a90929485bf1')
]

videos_dct = {v.slug: v for v in videos}
"""


def indice(request):
    videos = Video.objects.order_by('creation').all()  # traz todos os vídeos ordenados pela data de criação (do mais antigo para o mais novo)
    return render(request, 'aperitivos/indice.html', context={'videos': videos})


def video(request, slug):
    video = get_object_or_404(Video, slug=slug)
    return render(request, 'aperitivos/video.html', context={'video': video})
