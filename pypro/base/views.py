import logging
import random
from django.http import HttpResponse, HttpRequest


# Create your views here.
def home(request: HttpRequest):
    return HttpResponse(f'<html><body>Olá Django  This might not go well. result is {2 / 0} </body></html>  ', content_type='text/html')
