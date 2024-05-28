from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('kelahiran/', views.show_kelahiran, name='kelahiran'),
    path('kematian/', views.show_kematian, name='kematian'),
    path('kedatangan/', views.show_kedatangan, name='kedatangan'),
    path('kepindahan/', views.show_kepindahan, name='kepindahan'),
]