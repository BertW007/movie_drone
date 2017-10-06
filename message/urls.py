from django.conf.urls import url

from message import views

urlpatterns = [
    url(r'^user/(?P<pk>(\d)+)/message/$', views.MessageCreateView.as_view(), name='message-create'),
    url(r'^user/message/list/$', views.MessageListView.as_view(), name='message-view'),
    url(r'^user/message/delete/(?P<pk>(\d)+)/$', views.MessageDeleteView.as_view(),
        name='message-delete'),
]