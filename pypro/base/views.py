import logging
import random
from django.http import HttpResponse, HttpRequest


# Create your views here.
def home(request: HttpRequest):
    return HttpResponse(f'<html><body>Olá Django </body></html>  ', content_type='text/html')
