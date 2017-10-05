from django.conf.urls import url

from footage import views

urlpatterns = [
    url(r'^videos/$', views.FootageView.as_view(), name='footage-view'),
    url(r'^user/footage/add/$', views.FootageCreateView.as_view(), name='footage-create'),
    url(r'^user/footage/(?P<pk>(\d)+)/delete/$', views.FootageDeleteView.as_view(), name='footage-delete'),
    url(r'^user/footage/(?P<pk>(\d)+)/edit', views.FootageUpdateView.as_view(), name="footage-update"),
    url(r'^user/(?P<pk>(\d)+)/footage/detail/$', views.FootageDetailView.as_view(), name='footage-detail'),
    url(r'^user/(?P<pk>(\d)+)/footage/detail/add/$', views.FootageDetailCreateView.as_view(),
        name='footage-detail-create'),
    url(r'^user/(?P<pk>(\d)+)/footage/detail/edit/$', views.FootageDetailEditView.as_view(),
        name='footage-detail-edit'),
    url(r'^search/$', views.UserSearchView.as_view(), name='search'),

]