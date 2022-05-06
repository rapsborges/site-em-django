from django.shortcuts import render
from .models import Filme
from django.views.generic import TemplateView, ListView, DetailView


class Homepage(TemplateView):
    template_name = "homepage.html"


class Homefilmes(ListView):
    template_name = "homefilmes.html"
    model = Filme  # object_list -> Lista de itens do model


class Detalhesfilme(DetailView):
    template_name = "detalhesfilme.html"
    model = Filme # object -> 1 item do model









# Create your views here.
# def homepage(request):
#     return render(request, "homepage.html")


# def homefilmes(request):
#     context = {}
#     lista_filmes = Filme.objects.all()
#     context['lista_filmes'] = lista_filmes
#     return render(request, "homefilmes.html", context)