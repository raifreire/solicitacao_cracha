from django.urls import path
from apps.galeria.views import \
     index, imagem, buscar, novo_cracha, editar_cracha, deletar_cracha, filtro

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path('buscar', buscar, name='buscar'),
    path('novo-cracha', novo_cracha, name='novo_cracha'),
    path('editar-cracha/<int:foto_id>', editar_cracha, name='editar_cracha'),
    path('deletar-cracha/<int:foto_id>', deletar_cracha, name='deletar_cracha'),
    path('filtro/<str:categoria>', filtro, name='filtro'),
]