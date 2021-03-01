from rest_framework import viewsets
from rest_framework import permissions, authentication

from apps.produto.api.serializers import ProdutoSerializer
from apps.produto.models import Produto


class ProdutoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Produto.objects.all().order_by('-data_cadastro')
    serializer_class = ProdutoSerializer
    #permission_classes = [permissions.IsAuthenticated]
    #authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]

