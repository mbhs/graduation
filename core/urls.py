from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('success', views.success, name='success'),
    path('request', views.request, name='request'),
    path('donate', views.donate, name='donate'),
]