from django.shortcuts import render
from .models import BlogPost

class BlogDetailView(DetailView):
    model = BlogPost #Modelo usado pela view
    template_name = 'post.html' #Template para renderizar
    context_object_name = 'post' # Nome do contexto no template
