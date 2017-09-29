from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView

from footage.forms import FootageForm
from footage.models import Footage


class UserFootageCreateView(CreateView):
    model = Footage
    form_class = FootageForm

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
    pass