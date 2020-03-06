from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from .import views

app_name='analyse'

urlpatterns = [
    path('',views.analyse_data,name='analyse1'),
    path('charts-data/',views.charts_data,name='charts'),
    url(r'^aspects/(?P<finalst>[\w-]+)/(?P<spec>[\w-]+)/$',views.aspects_view,name='aspects'),
]
