from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import FormView

from footage.models import FootageDetail, Footage
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
            profile = Profile.objects.create(user=new_user)
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


class ConsoleView(LoginRequiredMixin, View):

    def get(self, request, pk):

        current_user = User.objects.get(pk=pk)
        if FootageDetail.objects.all().filter(person_id=pk).exists():
            details = FootageDetail.objects.get(person=current_user)
            edit_details = 'edit details'
            # cities = FootageDetail.objects.get(person_id=pk).city.all()

            return render(request, 'user/user_console.html', {
                'user': current_user,
                'details': details,
                'edit_details': edit_details,
                # 'cities': cities,
                'footage_list': Footage.objects.all().filter(author=pk)})

        else:
            add_details = 'add details'

            return render(request, 'user/user_console.html', {
                'user': current_user,
                'add_details': add_details,
                'footage_list': Footage.objects.all().filter(author=pk)
            })