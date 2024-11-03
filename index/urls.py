from django.urls import path
from index.views import index, textos, texto, buscar

urlpatterns = [
    path('', index, name='index'),
    path('textos/', textos, name='textos'),
    path('texto/<int:artigo_id>', texto, name='texto'),
    path("buscar/", buscar, name='buscar'),
]