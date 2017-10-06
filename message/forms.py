from django import forms

from message.models import Message, Recommendation


class MessageCreateForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']

class RecommendationCreateForm(forms.ModelForm):
    class Meta:
        model = Recommendation
        fields = ["content"]