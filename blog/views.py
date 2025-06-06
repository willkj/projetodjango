from django.shortcuts import render
from .models import BlogPost
from django.views.generic.detail import DetailView


class BlogDetailView(DetailView):
    model = BlogPost # Modelo usado pela view
    template_name = 'post.html' # Template para renderizar
    context_object_name = 'post' # Nome do contexto no template


blog = BlogDetailView.as_view()
