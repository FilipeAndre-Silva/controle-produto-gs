from rest_framework import serializers
from apps.produto.models import Produto


class ProdutoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Produto
        fields = ['url', 'id', 'descricao', 'data_validade', 'data_cadastro',
                  'data_atualizacao', 'qtd_estoque', 'preco_unid']

