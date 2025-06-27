from django.shortcuts import render


videos = [
    {'slug': 'motivacao', 'titulo': 'Video Aperitivo: Motivação', 'synthesia_id': '445f84c2-eb92-49da-a4dc-b4c0ec772fed'},
    {'slug': 'show', 'titulo': 'Video Aperitivo: Apresentação', 'synthesia_id': '8f1bdd22-99a8-4ca5-b615-a90929485bf1'}
]

videos_dct = {dct['slug']: dct for dct in videos}


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})


def video(request, slug):
    video = videos_dct[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
