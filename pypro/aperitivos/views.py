from django.shortcuts import render


# Create your views here.
def video(request, slug):
    video = {'titulo': 'Video Aperitivo: Motivação', 'synthesia_id': '445f84c2-eb92-49da-a4dc-b4c0ec772fed'}
    return render(request, 'aperitivos/video.html', context={'video': video})
