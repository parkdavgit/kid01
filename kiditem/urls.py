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
    url(r'^(?P<pk>[0-9]+)/cart_or_buy$', views.cart_or_buy, name='cart_or_buy'),
    url(r'^cart/(?P<pk>[0-9]+)/$', views.cart, name='cart'),
    url(r'^Norder_list/(?P<pk>[0-9]+)/$', views.Norder_list, name='Norder_list'),
]    