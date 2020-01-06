from django.forms import ModelForm
from .models import Comentario


class FormComentario(ModelForm):
    def clean(self):
        data = self.cleaned_data
        # print(data)
        nome = data.get('nome_comentario')
        email = data.get('email_comentario')
        comentario = data.get('nome_comentario_comentario')

        if len(nome)< 3:
            self.add_error(
               'nome_comentario',
                'Nome precisar ter mais de 3 caracteres'

            )
        if len(comentario) < 3:
            self.add_error(
                'nome_comentario_comentario',
                'Nome precisar ter mais de 3 caracteres'

            )
    class Meta:
        model = Comentario
        fields = ('nome_comentario', 'email_comentario', 'nome_comentario_comentario')
