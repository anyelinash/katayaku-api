from django.urls import path
from .views import (
    WhatsAppSettingsView, WhatsAppSettingsListView,
    send_whatsapp_message, send_whatsapp_file, consultar_api, listar_paths,
    obtener_path_por_id
)

urlpatterns = [
    path('whatsapp/', WhatsAppSettingsView.as_view(), name='whatsapp-settings'),
    path('whatsapp/list/', WhatsAppSettingsListView.as_view(), name='whatsapp-settings-list'),
    path('whatsapp/send-message/<str:id_instance>/', send_whatsapp_message, name='send-whatsapp-message'),
    path('whatsapp/send-file/<str:id_instance>/', send_whatsapp_file, name='send-whatsapp-file'),
    path('proveedor/<int:path_id>/<int:proveedor_id>/<str:valor>/', consultar_api, name='consultar_api'),
    path('proveedor/paths/', listar_paths, name='listar_paths'),
    path('proveedor/paths/<int:path_id>/', obtener_path_por_id, name='obtener_path_por_id'),
]