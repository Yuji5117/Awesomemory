from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from django import forms
from django.db.models import Q

from .forms import PostForm
from .models import Post, Comment, Category


CommentForm = forms.modelform_factory(Comment, fields=('text', ))


class IndexView(generic.ListView):
    model = Post
    template_name = 'post/post_list.html'
    context_object_name = 'post_list'
    paginate_by = 6

    # Search func
    def get_queryset(self):
        q_word = self.request.GET.get('query')

        if q_word:
            object_list = Post.objects.filter(
                Q(title__icontains=q_word)
            )
        else:
            object_list = Post.objects.all()

        return object_list


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # どのコメントにも紐づかないコメント=記事自体へのコメント を取得する
        context['comment_list'] = self.object.comment_set.filter(parent__isnull=True)
        return context

class PostCreate(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post/post_create.html'
    success_url = reverse_lazy('post:index')

class PostUpdate(generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post/post_create.html'
    success_url = reverse_lazy('post:index')
    

class PostDelete(generic.DeleteView):
    model = Post
    template_name = 'post/post_delete.html'
    success_url = reverse_lazy('post:index')
    

# Comment func
def comment_create(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    form = CommentForm(request.POST or None)

    if request.method == 'POST':
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        return redirect('post:post_detail', pk=post.pk)

    context = {
        'form': form,
        'post': post
    }
    return render(request, 'post/comment_form.html', context)

def reply_create(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    post = comment.post
    form = CommentForm(request.POST or None)

    if request.method == 'POST':
        reply = form.save(commit=False)
        reply.parent = comment
        reply.post = post
        reply.save()
        return redirect('post:post_detail', pk=post.pk)

    context = {
        'post': post,
        'form': form,
        'comment': comment
    }
    return render(request, 'post/comment_form.html', context)

