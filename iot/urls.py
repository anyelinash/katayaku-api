from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    # Modulos - General
    path('modulos', views.ModsView.as_view(), name='modulos'),
    path('modulo/<int:pk>', views.ModsDetailView.as_view()),

    # Registros
    # Rele
    path('releregistros', views.ReleView.as_view(), name='regisrele'),
    path('releregistro/<int:pk>', views.ReleDetailView.as_view()),

    # Sensor de flujo de agua
    path('aguaregistros', views.AguaView.as_view(), name='regisagua'),
    path('aguaregistro/<int:pk>', views.AguaDetailView.as_view()),

    # Sensor ultrasónico
    path('sonicoregistros', views.SonicView.as_view(), name='regisonicos'),
    path('sonicoregistro/<int:pk>', views.SonicDetailView.as_view()),

    # Sensor de calidad de aire
    path('airegistros', views.AireView.as_view(), name='regisaire'),
    path('airegistro/<int:pk>', views.AireDetailView.as_view()),

    # Alertas
    # Alertas Rele
    path('relealertas', views.AltReleView.as_view(), name='altrele'),
    path('relealerta/<int:pk>', views.AltReleDetailView.as_view()),

    # Alertas Sensor de flujo de agua
    path('agualertas', views.AltAguaView.as_view(), name='altagua'),
    path('agualerta/<int:pk>', views.AltAguaDetailView.as_view()),

    # Alertas Sensor ultrasónico
    path('sonicoalertas', views.AltSonicView.as_view(), name='altsonico'),
    path('sonicoalerta/<int:pk>', views.AltSonicDetailView.as_view()),

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
