from django.shortcuts import render, redirect, get_object_or_404, resolve_url
# for pagination #
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.views import generic
from django.urls import reverse_lazy
from django import forms
from django.db.models import Q

# 特定のログインユーザーしかページを見れないようにする、mixin and decorator #
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import PostForm, ImageForm, ImageModelFormSet
from .models import Post, Image



# # # 特定のログインユーザーしかページを見れないようにする、mixin #
# class OnlyYouMixin(UserPassesTestMixin):
#     # 条件に満たさない場合ログインページに移動 (Trueの場合、404ページを表示) #
#     raise_exeption = True

#     #  今ログインしているユーザーのpkと、ユーザー情報のpkが同じか、or superuserなら許可 #
#     def test_func(self):
#         user = self.request.user
#         return user.pk == self.kwargs['pk']


    
# paginator-function-view #
def paginator_queryset(request, queryset, count):

    # Pagenator: ex:paginator = Paginator(post(queryset), (count)3) #
    paginator = Paginator(queryset, count)
    page =request.GET.get('page')

    try:
        post_page = paginator.page(page)
    except PageNotAnInteger:
        post_page = paginator.page(1)
    except EmptyPage:
        post_page = paginator.page(paginator.num_pages)
    return post_page
# paginator-function-view #


@login_required
def post_list(request):
    posts = Post.objects.order_by('-created_at').filter(created_by=request.user)

    # search func #
    query = request.GET.get('query')
    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) | Q(category__name__icontains=query)
        )
        
    # page func #
    post_page = paginator_queryset(request, posts, 6)
    
    context = {
        'posts': post_page.object_list,
        'post_page': post_page
    }

    return render(request, 'post/post_list.html', context)



class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['image_list'] = Image.objects.all()
        return context


    # might use this later
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
    success_url = reverse_lazy('post:post')

    # Postモデルの(created_by_field)に(user_id)を自動的に追加する。  #
    def form_valid(self, form):
        form.instance.created_by_id = self.request.user.id
        return super().form_valid(form)



# to update post # 
class PostUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post/post_update.html'

    #  #
    def get_success_url(self):
        return resolve_url('post:post_detail', pk=self.kwargs['pk'])



# to delete post from post_list #
class PostDelete(LoginRequiredMixin, generic.DeleteView):
    model = Post
    template_name = 'post/post_delete.html'
    success_url = reverse_lazy('post:post')


# to create and update Image_model #
@login_required
def post_update_image(request, post_pk):
    ImageModelFormSet = forms.modelformset_factory(Image, form=ImageForm, fields=('multi_images', ), extra=9, max_num=12)
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST':
        formset = ImageModelFormSet(request.POST or None, request.FILES or None)
        if formset.is_valid():
            for form in formset:
                form = form.save(commit=False)
                form.post = post
                form.save() 
            messages.success(request, 'Updated!')
            return redirect('post:post_detail', pk=post.pk)
    else:
        formset = ImageModelFormSet(queryset=Image.objects.filter(post=post))

        # 引数にqueryset=Post.objects.none()を設定することでからのformだけを表示する #
        # formset = ImageModelFormSet(queryset=Post.objects.none())

    context = {
        'formset': formset
    }
    
    return render(request, 'post/post_update_image.html', context)


# Comment func
# def comment_create(request, post_pk):
#     CommentForm = forms.modelform_factory(Comment, fields=('text', ))
#     post = get_object_or_404(Post, pk=post_pk)
#     form = CommentForm(request.POST or None)

#     if request.method == 'POST':
#         comment = form.save(commit=False)
#         comment.post = post
#         comment.save()
#         return redirect('post:post_detail', pk=post.pk)

#     context = {
#         'form': form,
#         'post': post
#     }
#     return render(request, 'post/comment_form.html', context)


# repry method to comment #
# def reply_create(request, comment_pk):
#     CommentForm = forms.modelform_factory(Comment, fields=('text', ))
#     # get Comment model instead of Post #
#     comment = get_object_or_404(Comment, pk=comment_pk)
#     post = comment.post
#     form = CommentForm(request.POST or None)

#     if request.method == 'POST':
#         reply = form.save(commit=False)
#         reply.parent = comment
#         reply.post = post
#         reply.save()
#         return redirect('post:post_detail', pk=post.pk)

#     context = {
#         'post': post,
#         'form': form,
#         'comment': comment
#     }
#     return render(request, 'post/comment_form.html', context)

