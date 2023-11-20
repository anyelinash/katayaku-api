from django.urls import path
from . import views

urlpatterns = [
    # Empresa
    path('', views.IndexView.as_view(), name='index'),
    path('empresas', views.EmpView.as_view(), name='empresas'),
    path('empresa/<int:pk>', views.EmpDetailView.as_view()),

    # Usuario
    path('usuarios', views.UsuView.as_view(), name='usuarios'),
    path('usuario/<int:pk>', views.UsuDetailView.as_view()),

    path('usuarios/por_empresa/<str:cod_emp>/', views.UsuariosPorEmpresaView.as_view(), name='usuarios-por-empresa'),

    
    path('reportes', views.RepView.as_view(), name='reportes'),
    path('reporte/<int:pk>', views.RepDetailView.as_view())

]
