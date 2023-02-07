from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^notice/$', views.notice, name='notice'), 
    url(r'^detail/(?P<pk>[0-9]+)/$', views.notice_detail, name='notice_detail'),
    url(r'^product_detail/(?P<pk>[0-9]+)/$', views.product_detail, name='product_detail'),
]    