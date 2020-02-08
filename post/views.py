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

    # search post_list with title or category  #
    query = request.GET.get('query')
    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) | Q(category__icontains=query)
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
            if formset.deleted_forms:
                formset.save()
            messages.success(request, 'Updated!')
            return redirect('post:post_detail', pk=post.pk)
    else:
        formset = ImageModelFormSet(queryset=Image.objects.filter(post=post))

        # 引数にqueryset=Post.objects.none()を設定することでからのformだけを表示する #
        # formset = ImageModelFormSet(queryset=Post.objects.none())

    context = {
        'post': post,
        'formset': formset
    }
    
    return render(request, 'post/post_update_image.html', context)



