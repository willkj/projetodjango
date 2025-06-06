from django.db import models
from autoslug import AutoSlugField

# Create your models here.

class BlogPost(models.Model):
    # Define o titulo da postagem com um limite de 200 caracteres
    title = models.CharField(max_length=200, unique=True)

    # Cria automaticamente um slug com base no titulo
    slug = AutoSlugField(populate_from='title', unique=True, always_update=False)
    
    # O campo de texto para o conteúdo da postagem
    content = models.TextField()

    # Nome do autor da postagem
    author = models.CharField(max_length=100)

    # Data e hora em que a postagem foi criada
    created_at = models.DateTimeField(auto_now_add=True)

    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

