from django.urls import path
from . import views

urlpatterns = [
    # Empresa
    path('', views.IndexView.as_view(), name='index'),
    path('empresas', views.EmpView.as_view(), name='empresas'),
    path('empresa/<int:pk>', views.EmpDetailView.as_view()),

    # Usuario
    path('register/', views.UsuarioRegistrationView.as_view(), name='register'),
    path('login/', views.UsuarioLoginView.as_view(), name='login'),
    path('api/logout/', views.UsuarioLogoutView.as_view(), name='logout'),
    # path('login/', views.obtain_auth_token, name='api-token-auth'),
    path('usuarios', views.UsuListView.as_view(), name='usuarios'),
    path('usuario/<int:pk>', views.UsuDetailView.as_view()),


    
    path('reportes', views.RepView.as_view(), name='reportes'),
    path('reporte/<int:pk>', views.RepDetailView.as_view())

]
