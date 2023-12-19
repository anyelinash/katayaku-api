from django.test import TestCase
from .models import WhatsAppSettings, Path, Proveedor
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from rest_framework import status
from .models import WhatsAppSettings, Path, Proveedor
import json


class WhatsAppModelTest(TestCase):
    def test_whatsapp_settings_creation(self):
        whatsapp_settings = WhatsAppSettings.objects.create(
            id_instance='123',
            api_token_instance='abc123',
            name='Test Instance',
            description='Testing WhatsApp Settings',
            active=True,
        )
        self.assertEqual(str(whatsapp_settings), 'Test Instance')

    def test_path_creation(self):
        path = Path.objects.create(path='/test/path')
        self.assertEqual(str(path), '/test/path')

    def test_proveedor_creation(self):
        path = Path.objects.create(path='/test/path')
        proveedor = Proveedor.objects.create(
            token='token123',
            nombre='Test Proveedor',
            domain='example.com',
            descripcion='Proveedor de prueba',
        )
        proveedor.paths.add(path)
        self.assertEqual(str(proveedor), 'Test Proveedor')


# Puedes agregar más pruebas según sea necesario.


User = get_user_model()


class IotViewsTest(TestCase):
    def setUp(self):
        # Crear un usuario de prueba
        self.user = User.objects.create_user(
            correo='test@example.com',
            contrasena='testpassword',
            nombres='John',
            apellidos='Doe',
            dni='12345678',
            telefono='123456789',
            photo_url='https://example.com/photo.jpg',
        )
        # Crear un proveedor de prueba
        self.proveedor = Proveedor.objects.create(
            token='token123',
            nombre='Test Proveedor',
            domain='http://example.com',
            descripcion='Proveedor de prueba',
        )
        # Crear un path de prueba
        self.path = Path.objects.create(path='/test/path')

    def test_whatsapp_settings_view(self):
        client = Client()
        client.login(correo='test@example.com', contrasena='testpassword')

        response = client.get('/whatsapp/settings/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_send_whatsapp_message_view(self):
        client = Client()
        client.login(correo='test@example.com', contrasena='testpassword')

        whatsapp_settings = WhatsAppSettings.objects.create(
            id_instance='123',
            api_token_instance='abc123',
            name='Test Instance',
            description='Testing WhatsApp Settings',
            active=True,
            user=self.user,
        )

        data = {
            'chatId': '123456789',
            'message': 'Test message'
        }

        response = client.post(f'/whatsapp/send-message/{whatsapp_settings.id_instance}/', json.dumps(data),
                               content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_send_whatsapp_file_view(self):
        client = Client()
        client.login(correo='test@example.com', contrasena='testpassword')

        whatsapp_settings = WhatsAppSettings.objects.create(
            id_instance='123',
            api_token_instance='abc123',
            name='Test Instance',
            description='Testing WhatsApp Settings',
            active=True,
            user=self.user,
        )

        data = {
            'chatId': '123456789',
            'caption': 'Test caption'
        }

        response = client.post(f'/whatsapp/send-file/{whatsapp_settings.id_instance}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_consultar_api_view(self):
        client = Client()
        client.login(correo='test@example.com', contrasena='testpassword')

        response = client.get(f'/consultar-api/{self.path.id}/{self.proveedor.id}/test_value/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_listar_paths_view(self):
        client = Client()
        response = client.get('/listar-paths/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_obtener_path_por_id_view(self):
        client = Client()
        response = client.get(f'/obtener-path/{self.path.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

# Puedes agregar más pruebas según sea necesario.


from django.test import TestCase
from .models import WhatsAppSettings
from .serializers import WhatsAppSettingsSerializer


class IotSerializersTest(TestCase):
    def test_whatsapp_settings_serializer(self):
        data = {
            'id_instance': '123',
            'api_token_instance': 'abc123',
            'name': 'Test Instance',
            'description': 'Testing WhatsApp Settings',
            'active': True,
        }

        serializer = WhatsAppSettingsSerializer(data=data)
        self.assertTrue(serializer.is_valid())

        whatsapp_settings = serializer.save()
        self.assertEqual(whatsapp_settings.name, 'Test Instance')


# Puedes agregar más pruebas según sea necesario.
