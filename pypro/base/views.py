from django.http import HttpResponse


# Create your views here.
def home(response):
    return HttpResponse('<html><body>Olá Django </body></html>  ', content_type='text/html')
