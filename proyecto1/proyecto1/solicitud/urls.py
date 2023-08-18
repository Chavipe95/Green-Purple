from django.urls import path, re_path
from django.contrib.auth.views import LogoutView

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.LoginCustomView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('servidor', views.ServidorViews.as_view(), name='servidor'),
    path('reporte', views.ReportesView.as_view(), name='reporte'),
    path('perfil', views.perfil_view, name='perfil'),
    path('ajaxEditarReporte', views.editar_reporte, name='ajaxEditarReporte'),
    path('ajaxEliminarReporte', views.eliminar_reporte, name='ajaxEliminarReporte'),


]