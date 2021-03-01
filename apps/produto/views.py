from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, TemplateView
from rest_framework.authtoken.models import Token
from apps.produto.forms import ProdutoForms
from apps.produto.models import Produto


class ProdutoCreate(CreateView):
    model = Produto
    template_name = "produto/create.html"
    form_class = ProdutoForms

    def get_success_url(self):
        return reverse_lazy("listar_produto")


class ProdutoList(ListView):
    model = Produto
    paginate_by = 7
    template_name = "produto/list.html"


class ProdutoEdit(UpdateView):
    model = Produto
    template_name = "produto/edit.html"
    form_class = ProdutoForms

    def get_success_url(self):
        return reverse_lazy("listar_produto")


class ProdutoDetail(UpdateView):
    model = Produto
    template_name = "produto/detail.html"
    form_class = ProdutoForms


class ProdutoDelete(DeleteView):
    model = Produto
    template_name = "produto/delete.html"

    def get_success_url(self):
        return reverse_lazy("listar_produto")


class ServicoWebView(TemplateView):
    template_name = "produto/servico_web.html"

    def get_context_data(self, **kwargs):
        context = super(ServicoWebView, self).get_context_data(**kwargs)
        token = Token.objects.get(user=self.request.user)
        context['token_user'] = token

        return context