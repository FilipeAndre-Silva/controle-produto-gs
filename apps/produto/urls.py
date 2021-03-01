from django.contrib.auth.decorators import login_required
from django.urls import path
from apps.produto.views import *

urlpatterns = [
    path('criar/', login_required(ProdutoCreate.as_view()), name='criar_produto'),
    path('listar/', login_required(ProdutoList.as_view()), name='listar_produto'),
    path('editar/<int:pk>/', login_required(ProdutoEdit.as_view()), name='editar_produto'),
    path('detalhar/<int:pk>/', login_required(ProdutoDetail.as_view()), name='detalhar_produto'),
    path('deletar/<int:pk>/', login_required(ProdutoDelete.as_view()), name='deletar_produto'),

    path('servico_web/', login_required(ServicoWebView.as_view()), name='servico_web'),
]