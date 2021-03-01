from django import forms
from apps.produto.models import Produto


class ProdutoForms(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ProdutoForms, self).__init__(*args, **kwargs)

        self.fields['descricao'].widget.attrs['class'] = 'form-control'
        self.fields['data_validade'].widget.attrs['class'] = 'form-control'
        self.fields['qtd_estoque'].widget.attrs['class'] = 'form-control'
        self.fields['preco_unid'].widget.attrs['class'] = 'form-control'