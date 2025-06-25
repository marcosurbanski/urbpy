from django.shortcuts import render


# Create your views here.
def video(request, slug):
    videos = {
        'motivacao': {'titulo': 'Video Aperitivo: Motivação', 'synthesia_id': '445f84c2-eb92-49da-a4dc-b4c0ec772fed'},
        'show': {'titulo': 'Video Aperitivo: Apresentação', 'synthesia_id': '8f1bdd22-99a8-4ca5-b615-a90929485bf1'}
    }
    video = videos[slug]
    video['slug'] = slug
    return render(request, 'aperitivos/video.html', context={'video': video})
