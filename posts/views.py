from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from .models import Post

# anotede
from django.db.models import Q, Count, Case, When


# Create your views here.
class PostIndex(ListView):
    template_name = 'posts/index.html '
    paginate_by = 2
    model = Post
    context_object_name = 'posts'

    def get_queryset(self):
        query = super().get_queryset()
        query = query.order_by('-id').filter(publicado_post=True)
        query = query.annotate(
            # contar apenas os comentarios ativos
            numero_comentario=Count(
                Case(
                    When(comentario__publicado_comentario=True, then=1)
                )
            )
        )
        return query


class PostBusca(PostIndex):
    template_name = 'posts/post_busca.html'

    def get_queryset(self):
        query = super().get_queryset()
        # print(self.request.GET.get('termo'))
        termo = self.request.GET.get('termo')

        if not termo:
            return query

        query = query.filter(
            Q(titulo_post__icontains=termo)
            | Q(autor_post__first_name__iexact=termo) #esse deu erro
            | Q(conteudo_post__icontains=termo)
            | Q(excerto_post__icontains=termo)
            | Q(categoria_post__nome_cat__iexact=termo)
            # Q(categoria_post__iexact=termo)
        )
        return query


class PostCategoria(PostIndex):
    template_name = 'posts/post_categoria.html'

    def get_queryset(self):
        query = super().get_queryset()
        categoria = self.kwargs.get('categoria', None)
        if not categoria:
            return query

        query = query.filter(categoria_post__nome_cat__iexact=categoria)
        return query


class PostDetalhes(UpdateView):
    pass
