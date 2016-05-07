from django.conf.urls import url#, include
from .views import IndexView, UsuarioView, GreetView, DateView,JsonView, ColorView, ColorsView
from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
    url(r'index/$', csrf_exempt(IndexView.as_view())),
    url(r'usuario/$', csrf_exempt(UsuarioView.as_view())),
    url(r'greet/([a-z]+)$', csrf_exempt(GreetView.as_view())),
    url(r'greet/([a-z]+)/([a-z]+)$', csrf_exempt(GreetView.as_view())),
    url(r'date/(\d+)/(\d+)/(\d+)$', csrf_exempt(DateView.as_view())),
    url(r'json/$', csrf_exempt(JsonView.as_view())),
    url(r'color/([a-z]+)/$', csrf_exempt(ColorView.as_view())),
    url(r'colors/$', csrf_exempt(ColorsView.as_view()))
]