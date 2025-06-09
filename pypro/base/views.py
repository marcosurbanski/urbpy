import logging
import random
from django.http import HttpResponse, HttpRequest


# Create your views here.
def home(response):
    return HttpResponse('<html><body>Olá Django </body></html>  ', content_type='text/html')
