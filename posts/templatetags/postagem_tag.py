from django import template

register = template.Library()


@register.filter(name='plural_comentario')
def plural_comentario(num_comentario):
    num_comentario = int(num_comentario)
    if num_comentario <= 1:
        resposta = f'{num_comentario} Comentario'
    else:
        resposta = f'{num_comentario} Comentarios'
    return resposta
