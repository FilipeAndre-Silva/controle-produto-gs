from allauth.account.forms import LoginForm


class FormularioLogin(LoginForm):

    def __init__(self, *args, **kwargs):
        super(FormularioLogin, self).__init__(*args, **kwargs)

        self.fields['login'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['login'].widget.attrs['placeholder'] = 'Email'
        self.fields['password'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['password'].widget.attrs['placeholder'] = 'Senha'