from django.db import models

class Texto(models.Model):
    titulo = models.CharField(max_length=100, null=False, blank=False)
    sub_titulo = models.CharField(max_length=100, null=False, blank=False)
    data_postagem = models.DateField(auto_now=False, auto_now_add=True)
    conteudo = models.TextField()
    imagem = models.ImageField(upload_to='imagens/%Y/%m/%d/', blank=True)
    visivel = models.BooleanField(default=True)

    def __str__(self):
        return f'Titulo: {self.titulo} - {self.sub_titulo}'

