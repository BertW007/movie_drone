from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView

from footage.forms import FootageForm, FootageDetailCreateForm, FootageDetailEditForm
from footage.models import Footage, FootageDetail


class FootageCreateView(CreateView):
    model = Footage
    form_class = FootageForm
    template_name = 'footage/footage_create_form.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        url = obj.link
        if len(url) > 35:
            obj.link = url.replace("watch?v=", "embed/")
        else:
            obj.link = url.replace("https://youtu.be", "https://www.youtube.com/embed")
        obj.author = self.request.user
        obj.save()
        return HttpResponseRedirect(reverse('main'))


class FootageUpdateView(UpdateView):
    model = Footage
    form_class = FootageForm


class FootageDeleteView(DeleteView):
    model = Footage
    template_name = 'footage/footage_delete_form.html'

    def get_success_url(self):
        return reverse ('console', kwargs= {
            'pk': int(self.request.user.id)
        })

class FootageView(View):
    model = Footage
    template_name = 'footage/footage_view.html'

    def get(self,request):
        footage = Footage.objects.all().order_by('-id')
        return render(request, 'footage/footage_view.html', {
            'footage': footage
        })


class FootageDetailView(View):
    def get(self, request, pk):
        current_user = User.objects.get(pk=pk)
        if FootageDetail.objects.all().filter(person_id=pk).exists():
            detail = FootageDetail.objects.get(person=current_user)
            city = FootageDetail.objects.get(person_id=pk).city.all()
            return render(request, 'footage/footage_detail_view.html', {
                'user': current_user,
                'city': city,
                'detail': detail,
                'footage_list': Footage.objects.all().filter(author= pk)})
        else:
            return render(request, 'footage/footage_detail_view.html', {
                'user': current_user,
                'footage_list': Footage.objects.all().filter(author= pk)})


class FootageDetailCreateView(CreateView):
    model = FootageDetail
    form_class = FootageDetailCreateForm
    template_name = 'footage/footage_detail_create_form.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.person = self.request.user
        obj.save()
        return HttpResponseRedirect(reverse('footage-view'))


class FootageDetailEditView(UpdateView):
    model = FootageDetail
    form_class = FootageDetailEditForm
    template_name = 'footage/footage_detail_create_form.html'

    def get_object(self):
        return self.request.user.footagedetail