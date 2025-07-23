from django.urls import path
from pypro.base.views import home
from .views import CustomLoginView

app_name = 'base'
urlpatterns = [
    path('', home, name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
]
