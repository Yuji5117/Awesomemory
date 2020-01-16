from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin


from .forms import SignupForm, ProfileForm, UserUpdateForm, ProfileUpdateForm
from .models import UserProfile

class SignupView(CreateView):
    form_class = SignupForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    # def form_valid(self, form):
    #     user = form.save()
    #     login(self.request, user)
    #     self.object = user
    #     return HttpResponseRedirect(self.get_success_url())


    # Login automatically after signup #
    # def form_valid(self, form):
    #     super().form_valid(form)
    #     login(self.request, self.form)
    #     return valid

class UserProfileView(LoginRequiredMixin, DetailView):
    model = UserProfile
    template_name = 'registration/user_profile.html'


class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = ProfileUpdateForm
    template_name = 'registration/user_profile_update.html'
    # success_url = reverse_lazy('accounts:profile')

    def get_success_url(self):
        return resolve_url('accounts:profile', pk=self.kwargs['pk'])





# def update_profile(request, pk):
#     # u_form = UserUpdateForm

#     #  もしrequestがPOSTだったら元々あるインスタンス、リクエスト内容とファイルを受け取る #
#     if request.method == 'POST':
#         profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)

#         #  バリデーションを行う OKならsave #
#         if profile_form.is_valid():
#             profile_form.save()
#             messages.success(request, f'Your account has been updated!!')
#             return redirect('accounts:profile')
#     # if not  元々あるインスタンスだけを返す #
#     else:
#         profile_form = ProfileUpdateForm(instance=request.user.userprofile)
#     context = {
#         # 'u_form': u_form,
#         'profile_form': profile_form
#     }
#     return render(request, 'registration/user_profile_update.html', context)
