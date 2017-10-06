from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView, DeleteView

from message.forms import MessageCreateForm
from message.models import Message


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageCreateForm
    template_name = 'message/message_create_form.html'
    raise_exception = True

    def form_valid(self, form):
        message = form.save(commit=False)
        message.sender = self.request.user
        message.receiver = User.objects.get(pk=self.kwargs['pk'])
        message.save()
        return HttpResponseRedirect(reverse('footage-detail', kwargs={
            'pk': int(self.kwargs['pk'])}
        ))


class MessageListView(LoginRequiredMixin, View):

    def get(self, request):
        messages_received = Message.objects.all().filter(receiver=self.request.user)
        messages_sent = Message.objects.all().filter(sender=self.request.user)
        return render(request, 'message/message_view.html', {
            'messages_received': messages_received,
            'messages_sent': messages_sent,
        })

class MessageDeleteView(DeleteView):
    model = Message
    template_name = 'message/message_delete_form.html'

    def get_success_url(self):
        return reverse('message-view')