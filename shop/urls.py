from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ProductList, name='ProductList'),
    url(r'^(?P[-\w]+)/$', views.ProductList, name='ProductListByCategory'),
    url(r'^(?P\d+)/(?P[-\w]+)/$', views.ProductDetail, name='ProductDetail'),
]