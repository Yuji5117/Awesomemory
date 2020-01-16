from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from django.views import generic
from django.urls import reverse_lazy
from django import forms
from django.db.models import Q
# 特定のログインユーザーしかページを見れないようにする、mixin #
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

from .forms import PostForm, PostModelFormSet
from .models import Post, Comment, Category


CommentForm = forms.modelform_factory(Comment, fields=('text', ))


# # 特定のログインユーザーしかページを見れないようにする、mixin #
# class OnlyYouMixin(UserPassesTestMixin):
#     # 条件に満たさない場合ログインページに移動 (Trueの場合、404ページを表示) #
#     raise_exeption = True

#     #  今ログインしているユーザーのpkと、ユーザー情報のpkが同じか、or superuserなら許可 #
#     def test_func(self):
#         user = self.request.user
#         return user.pk == self.kwargs['pk'] or user.is_superuser



class IndexView(LoginRequiredMixin, generic.ListView):
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


class PostDetail(LoginRequiredMixin, generic.DetailView):
    model = Post
    template_name = 'post/post_detail.html'

    # commentモデルを追加 #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # どのコメントにも紐づかないコメント=記事自体へのコメント を取得する
    #     context['comment_list'] = self.object.comment_set.filter(parent__isnull=True)
    #     return context


class PostCreate(LoginRequiredMixin, generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post/post_create.html'
    success_url = reverse_lazy('post:index')


def multi_upload(request):
    post = request.POST or None
    files = request.FILES or None
    #  すでにアップロード済みのファイルは表示しないという設定 #
    queryset = Post.objects.none()

    formset = PostModelFormSet(post, files, queryset)

    if request.method == 'POST' and formset.is_valid():
        formset.save()
        return redirect('post:index')

    context = {
        'formset': formset
    }
    return render(request, 'post/post_create.html', context)



class PostUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post/post_create.html'

    #  #
    def get_success_url(self):
        return resolve_url('post:post_detail', pk=self.kwargs['pk'])
    

class PostDelete(LoginRequiredMixin, generic.DeleteView):
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


# repry method to comment #
def reply_create(request, comment_pk):
    # get Comment model instead of Post #
    comment = get_object_or_404(Comment, pk=comment_pk)
    post = comment.post
    form = CommentForm(request.POST or None)

    if request.method == 'POST':
        reply = form.save(commit=False)
        reply.parent = comment
        reply.post = post
        reply.save()
        return redirect('post:post_detail', pk=post.pk)

#     context = {
#         'post': post,
#         'form': form,
#         'comment': comment
#     }
#     return render(request, 'post/comment_form.html', context)

