from allauth.account.views import LoginView, LogoutView
from django.urls import path
from django.views.generic import RedirectView

from apps.autenticacao.forms import FormularioLogin

urlpatterns = [
    path('login/', LoginView.as_view(template_name='autenticacao/login.html',
                                     form_class=FormularioLogin), name='account_login'),

    path('logout/', LogoutView.as_view(template_name='autenticacao/logout.html'), name='account_logout'),

    path('', RedirectView.as_view(url='login', permanent=True), name='account_signup'),
]