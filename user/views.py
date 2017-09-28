from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import FormView

from user.forms import UserCreateForm, UserEditForm, ProfileEditForm, UserLoginForm
from user.models import Profile


class UserCreateView(View):
    def get(self, request):
        form = UserCreateForm()
        return render(request, 'user/user_create_form.html', {
            'form': form
        })

    def post(self, request):
        form = UserCreateForm(data=request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request, 'user/user_create_done.html', {
                'new_user': new_user
            })


class UserEditView(LoginRequiredMixin, View):

    def get(self, request):
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        return render(request, 'user/user_edit_form.html', {
            'user_form': user_form,
            'profile_form': profile_form,
        })

    def post(self, request):
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                       data=request.POST,
                                       files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
        return render(request, 'user/user_edit_form.html', {
            'user_form': user_form,
            'profile_form': profile_form,
        })


class UserLoginView(FormView):
    form_class = UserLoginForm
    template_name = 'user/user_login_form.html'

    def form_valid(self, form):
        login(self.request, form.user)
        return redirect(self.request.GET.get('next', '/'))


class UserLogoutView(View):
    def get(self, request):
        logout(self.request)
        return redirect('/')