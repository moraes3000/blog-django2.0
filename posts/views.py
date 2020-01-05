from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from .models import Post

# Create your views here.
class PostIndex(ListView):
    template_name = 'posts/index.html '
    paginate_by = 2
    model = Post


class PostBusca(PostIndex):
    pass


class PostCategoria(PostIndex):
    pass


class PostDetalhes(UpdateView):
    pass
