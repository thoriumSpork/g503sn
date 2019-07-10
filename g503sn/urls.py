from django.conf.urls import url
from django.urls import path
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('jeeps/', views.JeepListView.as_view(), name='jeeps'),
    url(r'^(?P<jeep_id>[0-9]+)/$', views.detail, name='detail'),
]