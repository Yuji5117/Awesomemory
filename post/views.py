from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.urls import reverse_lazy
from itertools import chain
from django import forms
from django.db.models import Q
# 特定のログインユーザーしかページを見れないようにする、mixin #
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

from .forms import PostForm, ImageForm, ImageModelFormSet
from .models import Post, Comment, Category, Image


CommentForm = forms.modelform_factory(Comment, fields=('text', ))


# # 特定のログインユーザーしかページを見れないようにする、mixin #
class OnlyYouMixin(UserPassesTestMixin):
    # 条件に満たさない場合ログインページに移動 (Trueの場合、404ページを表示) #
    raise_exeption = True

    #  今ログインしているユーザーのpkと、ユーザー情報のpkが同じか、or superuserなら許可 #
    def test_func(self):
        user = self.request.user
        return user.pk == self.kwargs['pk']

    

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



@login_required
def post_list(request):
    posts = Post.objects.order_by('-created_by').filter(created_by=request.user)

    # search func #
    query = request.GET.get('query')
    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) | Q(category__name__icontains=query)
        )
        
    # page func #
    post_page = paginator_queryset(request, posts, 3)
    
    context = {
        'posts': post_page.object_list,
        'post_page': post_page
    }

    return render(request, 'post/post_list.html', context)



class PostDetail(generic.DetailView):
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
    success_url = reverse_lazy('post:post')

    # Postモデルのcreated_by fieldにuser_id　を自動的に追加する。  #
    def form_valid(self, form):
        form.instance.created_by_id = self.request.user.id
        return super().form_valid(form)




# class PostAddUpdate(generic.CreateView):
#     model = Post
#     form_class = ImageForm
#     template_name = 'post/post_add_image.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(*kwargs)
#         if request.method == 'POST':
#             context['formset'] = ImageModelFormSet(request.Post, request.FILES)
#         else:
#             context['formset'] = ImageModelFormSet()
#         return context


#     def form_valid(self, form):
#         context = self.get_context_data()
#         formset = context['formset']
#         if formset.is_valid():
#             # self.object = form.save(commit=False)
#             # self.object.user = self.request.user
#             self.object.save()

#             formset.instance = self.object
#             formset.save()
            
#             return redirect('post:post_detail')



    

# def post_create(request):
#     ImageModelFormSet = forms.modelformset_factory(Image, form=ImageForm, fields=('multi_images', ), extra=5, max_num=5)
#     if request.method == 'POST':
#         post = PostForm(request.POST)
#         # image or file 保存する場合　引数にrequest.FILESが必要 #
#         formsets = ImageModelFormSet(request.POST or None, request.FILES or None)

#         if formsets.is_valid():
#             post = post.save(commit=False)
#             post.created_by = request.user
#             post.save()
#             for formset in formsets:
#                 # commit=False = データベースへ保存する前のモデルインスタンスのリストを取得
#                 multi_images = formset['multi_images']
#                 image = Image(post=post, multi_images=multi_images)
#                 image.save() 
#             messages_success(request, 'Created!')
#             return redirect('post:post')
#     else:
#         post = PostForm()
#         # 引数にqueryset=Post.objects.none()を設定することでからのformだけを表示する #
#         formsets = ImageModelFormSet(queryset=Post.objects.none())

#     context = {
#         'post': post,
#         'formsets': formsets
#     }
    
#     return render(request, 'post/post_create.html', context)



# def multi_upload(request):
#     post = request.POST or None
#     files = request.FILES or None
#     #  すでにアップロード済みのファイルは表示しないという設定 #
#     queryset = Post.objects.none()

#     formset = PostModelFormSet(post, files, queryset)

#     if request.method == 'POST' and formset.is_valid():
#         formset.save()
#         return redirect('post:index')

#     context = {
#         'formset': formset
#     }
#     return render(request, 'post/post_create.html', context)



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

