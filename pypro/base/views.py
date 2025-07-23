from django.shortcuts import render
import requests
from django.conf import settings
from django.contrib.auth.views import LoginView
from django.http import HttpResponseForbidden


# Create your views here.
def home(request):
    return render(request, 'base/home.html')


class CustomLoginView(LoginView):
    template_name = "registration/login.html"  # seu template

    def form_valid(self, form):
        token = self.request.POST.get("cf-turnstile-response")
        if not token:
            return HttpResponseForbidden("Captcha não preenchido.")

        data = {
            "secret": settings.CLOUDFLARE_TURNSTILE_SECRET,
            "response": token,
            "remoteip": self.request.META.get("REMOTE_ADDR"),
        }

        resp = requests.post("https://challenges.cloudflare.com/turnstile/v0/siteverify", data=data)
        result = resp.json()

        if not result.get("success"):
            return HttpResponseForbidden("Captcha inválido.")

        return super().form_valid(form)
