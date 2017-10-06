from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.base import TemplateResponseMixin

from footage.forms import FootageForm, FootageDetailCreateForm, FootageDetailEditForm, UserSearchForm
from footage.models import Footage, FootageDetail
from message.models import Message
from user.models import Profile


class FootageCreateView(PermissionRequiredMixin, CreateView):
    model = Footage
    form_class = FootageForm
    template_name = 'footage/footage_create_form.html'
    permission_required = 'footage.add_footage'
    raise_exception = True

    def get_queryset(self):
        qs = super(FootageCreateView, self).get_queryset()
        return qs.filter(author=self.request.user)


    def form_valid(self, form):
        obj = form.save(commit=False)
        url = obj.link
        if len(url) > 35:
            obj.link = url.replace("watch?v=", "embed/")
        else:
            obj.link = url.replace("https://youtu.be", "https://www.youtube.com/embed")
        obj.author = self.request.user
        obj.save()
        return HttpResponseRedirect(reverse('footage-view'))


class FootageUpdateView(PermissionRequiredMixin, UpdateView):
    model = Footage
    form_class = FootageForm
    template_name = 'footage/footage_create_form.html'
    success_url = reverse_lazy('user-console')
    permission_required = 'footage.change_footage'
    raise_exception = True

    def get_queryset(self):
        qs = super(FootageUpdateView, self).get_queryset()
        return qs.filter(author=self.request.user)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(FootageUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('user-console', kwargs={
            'pk': int(self.request.user.id)
        })


class FootageDeleteView(PermissionRequiredMixin, DeleteView):
    model = Footage
    template_name = 'footage/footage_delete_form.html'
    success_url = reverse_lazy('user-console')
    permission_required = 'footage.delete_footage'
    raise_exception = True

    def get_queryset(self):
        qs = super(FootageDeleteView, self).get_queryset()
        return qs.filter(author=self.request.user)

    def get_success_url(self):
        return reverse ('user-console', kwargs= {
            'pk': int(self.request.user.id)
        })

class FootageView(View):
    model = Footage
    template_name = 'footage/footage_view.html'

    def get(self, request):

        ctx = {
            'object_list': Footage.objects.all().order_by("-id"),
        }
        return render(request, 'footage/footage_view.html', ctx)


class FootageDetailView(LoginRequiredMixin, View):
    def get(self, request, pk):
        current_user = User.objects.get(pk=pk)
        if FootageDetail.objects.all().filter(person_id=pk).exists():
            detail = FootageDetail.objects.get(person=current_user)
            return render(request, 'footage/footage_detail_view.html', {
                'user': current_user,
                'detail': detail,
                'footage_list': Footage.objects.all().filter(author= pk)})
        else:
            return render(request, 'footage/footage_detail_view.html', {
                'user': current_user,
                'footage_list': Footage.objects.all().filter(author= pk)})


class FootageDetailCreateView(PermissionRequiredMixin, CreateView):
    model = FootageDetail
    form_class = FootageDetailCreateForm
    template_name = 'footage/footage_detail_create_form.html'
    # success_url = reverse_lazy('user-console')
    permission_required = 'footage.add_footage'
    raise_exception = True

    def hande_no_permission(self):
        if self.request.user.is_authenticated and self.raise_exception:
            return HttpResponseForbidden()
        else:
            return redirect(settings.LOGIN_URL)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.person = self.request.user
        obj.save()
        return HttpResponseRedirect(reverse('footage-view'))

    # def get_success_url(self):
    #     return reverse('user-console', kwargs={
    #         'pk': int(self.request.user.id)
    #     })


class FootageDetailEditView(PermissionRequiredMixin, UpdateView):
    model = FootageDetail
    form_class = FootageDetailEditForm
    template_name = 'footage/footage_detail_create_form.html'
    success_url = reverse_lazy('user-console')
    permission_required = 'footage.change_footage'
    raise_exception = True

    def get_object(self):
        return self.request.user.footagedetail

    def hande_no_permission(self):
        if self.request.user.is_authenticated and self.raise_exception:  # jezeli jestes zalogowany i nie masz uprwanien, 403
            return HttpResponseForbidden()
        else:
            return redirect(settings.LOGIN_URL)

    def get_success_url(self):
        return reverse('user-console', kwargs={
            'pk': int(self.request.user.id)
        })


class UserSearchView(FormView):
    template_name = 'footage/user_search_form.html'
    form_class = UserSearchForm

    def form_valid(self, form):
        city_name = form.cleaned_data['city']
        pricing = form.cleaned_data['maximum_price']
        filtered_details = FootageDetail.objects.filter(city=city_name).filter(pricing__lt=pricing)

        return render(self.request, self.template_name, {
            'form': form,
            'details': filtered_details,
        })