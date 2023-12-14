from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    # prueba
    path('reles/', views.ReleListCreateView.as_view(), name='rele-list-create'),
    path('reles/<int:pk>/', views.RelayDetailView.as_view(), name='rele-detail'),

    # Modulos - General
    path('modulos', views.ModsView.as_view(), name='modulos'),
    path('modulo/<int:pk>', views.ModsDetailView.as_view()),

    # Registros
    # Rele
    path('releregistros', views.ReleView.as_view(), name='regisrele'),
    path('releregistro/<int:pk>', views.ReleDetailView.as_view()),

    # control de estado del relé
    path('relay/', views.RelayControlView.as_view(), name='relay-control'),

    # Sensor de calidad de aire
    path('airegistros', views.AireView.as_view(), name='regisaire'),
    path('airegistro/<int:pk>', views.AireDetailView.as_view()),

    # Alertas
    # Alertas Rele
    path('relealertas', views.AltReleView.as_view(), name='altrele'),
    path('relealerta/<int:pk>', views.AltReleDetailView.as_view()),

    # Alertas Sensor de calidad de aire
    path('airealertas', views.AltAireView.as_view(), name='altaire'),
    path('airealerta/<int:pk>', views.AltAireDetailView.as_view()),

    # mantenimientos
    path('mantenimientos', views.MantemimientoView.as_view(), name='mantenimientos'),
    path('mantenimiento/<int:pk>', views.MantemimientoDetailView.as_view()),

    # temporizadores
    path('temporizadores', views.TemporizadoresView.as_view(), name='temporizadores'),
    path('temporizador/<int:pk>', views.TemporizadoresDetailView.as_view()),

]
