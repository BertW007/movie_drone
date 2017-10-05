from django.conf.urls import url

from user import views

urlpatterns = [
    url(r'^login/$', views.UserLoginView.as_view(), name='user-login'),
    url(r'^logout/', views.UserLogoutView.as_view(), name='user-logout'),
    url(r'^register/$', views.UserCreateView.as_view(), name='user-create'),
    url(r'^register/done/$', views.UserCreateView.as_view(), name='user-create-done'),
    url(r'^profile/edit/$', views.UserEditView.as_view(), name='user-edit'),
    url(r'^(?P<pk>(\d)+)/profile/console/$', views.ConsoleView.as_view(), name='user-console'),
]