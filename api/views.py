from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
import json
from .models import Colors
# Create your views here.

def index(request):
    return HttpResponse("INDEX")

class HomeView(View):
    def get(self, request):
        return HttpResponse("Esto es una vista")

class IndexView(View):
    def get(self, request):
        get_params = request.GET
        nombre = get_params.get("nombre", "Indefinido")
        return HttpResponse("Esto es el index del API\nNombre: "+nombre)
    def post(self, request):
        post_params = request.POST
        nombre = post_params.get("nombre", "Indefinido")
        return HttpResponse("Método POST llamado\nNombre: "+nombre)

class UsuarioView(View):
    def get(self, request):
        get_params = request.GET
        nombre = get_params.get("nombre","Indefinido")
        return HttpResponse("<h1>GET UsuarioView</h1>: "+nombre)
    def post(self, request):
        post_params = request.POST
        nombre = post_params.get("nombre","Indefinido")
        return HttpResponse("POST UsuarioView: "+nombre)
    def put(self, request):
        return HttpResponse("PUT UsuarioView")
    def delete(self, request):
        return HttpResponse("DELETE UsuarioView")

class GreetView(View):
    def get(self, request, nombre, apellido = "Juan"):
        return HttpResponse("<h1>Hola: "+nombre+ " - " + apellido +"</h1>")

class DateView(View):
    def get(self, request, dia, mes, anio):
        return HttpResponse("Fecha: " + dia + "/" + mes + "/" + anio)
#   def get(self, request, nombre):
#        return HttpResponse("<h1>Hola: "+nombre+"</h1>")

class JsonView(View):
    def get(self, request):
        return HttpResponse("""
        {
            "grupo": "Cinta Negra",
            "integrante": ["Salvador", "Ivan", "Hector"]
        }
        """, content_type='application/json')

    def post(self, request):
        my_json = {
            'colors': [
                '#000000',
                '#FFFFFF',
                '#FF0000'
            ]
        }
        color = request.POST.get('color')
        if color:
            my_json['colors'].append(color)
        return HttpResponse(json.dumps(my_json), content_type='application/json')


class ColorView(View):

    colores = {
        'rojo': '#FF0000',
        'azul': '#0000FF'
    }

    def get(self, request, color):
        print(color)
        hex = self.colores.get(color)
        if hex:
            resp = {'status': 'ok', 'hex': hex}
        else:
            resp = {'status': 'error', 'message': 'Color not available'}

        return HttpResponse(json.dumps(resp), content_type='application/json')

class ColorsView(View):
    def get(self,request):
        list_color = []
        colors = Colors.objects.all()
        for c in colors:
            dic_color = {
                'name' : c.name
            }
            list_color.append(dic_color)
            print(type(c))

        return HttpResponse(json.dumps(list_color), content_type='application/json')