from django.test import TestCase
from datetime import datetime
from users.models import Usuario, Empresa
from .models import Modulo, RegistrosRele, RegistrosAgua, RegistrosUltrasonico, RegistrosAire, AlertasRele, AlertasAire, \
    Mantenimientos, Temporizadores
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from rest_framework import status
import json
from django.test import TestCase
from .models import Rele, Modulo, RegistrosRele, RegistrosAire, AlertasRele, AlertasAire, Mantenimientos, Temporizadores
from .serializer import RelaySerializer, ModuloSerializer, ReleSerializer, AireSerializer, AlertReleSerializer, \
    AlertAireSerializer, MantenimientoSerializer, TemporizadorSerializer


class IotModelTest(TestCase):
    def setUp(self):
        # Crear un usuario y empresa de prueba
        self.user = Usuario.objects.create_user(
            correo='test@example.com',
            contrasena='testpassword',
            nombres='John',
            apellidos='Doe',
            dni='12345678',
            telefono='123456789',
            photo_url='https://example.com/photo.jpg',
        )
        self.empresa = Empresa.objects.create(
            codigo_usu=self.user,
            numero='123',
            nombre_o_razon_social='Empresa de Prueba',
            tipo_contribuyente='Contribuyente',
            estado='Activo',
            condicion='Regular',
            departamento='Lima',
            provincia='Lima',
            distrito='Miraflores',
            direccion='Av. Prueba 123',
            direccion_completa='Av. Prueba 123, Miraflores, Lima',
        )

    def test_modulo_creation(self):
        modulo = Modulo.objects.create(
            codigo_usu=self.user,
            nombre='Modulo de Prueba',
            ubicacion='Ubicacion de Prueba',
            descripcion='Descripción de Prueba',
            estado=True,
        )
        self.assertEqual(str(modulo), 'Modulo de Prueba')

    def test_registros_rele_creation(self):
        modulo = Modulo.objects.create(
            codigo_usu=self.user,
            nombre='Modulo de Prueba',
            ubicacion='Ubicacion de Prueba',
            descripcion='Descripción de Prueba',
            estado=True,
        )
        registro_rele = RegistrosRele.objects.create(
            is_on=True,
            cod_modulo=modulo,
            fecha_hora=datetime.now(),
        )
        self.assertEqual(str(registro_rele), f'Registro de Relé {registro_rele.cod_registro}')

    def test_registros_agua_creation(self):
        modulo = Modulo.objects.create(
            codigo_usu=self.user,
            nombre='Modulo de Prueba',
            ubicacion='Ubicacion de Prueba',
            descripcion='Descripción de Prueba',
            estado=True,
        )
        registro_agua = RegistrosAgua.objects.create(
            cod_modulo=modulo,
            fecha_hora=datetime.now(),
            flujo=10.5,
            unidadmedida='Litros',
            nivelflujo='Alto',
        )
        self.assertEqual(str(registro_agua), f'Registro de Agua {registro_agua.cod_registro}')

    # Puedes seguir creando pruebas para los otros modelos.


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

    def test_rele_list_create_view(self):
        client = Client()
        client.login(correo='test@example.com', contrasena='testpassword')

        data = {
            'nombre': 'Test Rele',
            'topico': 'test/topic',
            'status': True
        }

        response = client.post('/rele/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_rele_detail_view(self):
        client = Client()
        client.login(correo='test@example.com', contrasena='testpassword')

        rele = Rele.objects.create(nombre='Test Rele', topico='test/topic', status=True)

        response = client.get(f'/rele/{rele.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_rele_detail_update_view(self):
        client = Client()
        client.login(correo='test@example.com', contrasena='testpassword')

        rele = Rele.objects.create(nombre='Test Rele', topico='test/topic', status=True)

        data = {
            'nombre': 'Updated Rele',
            'topico': 'updated/topic',
            'status': False
        }

        response = client.put(f'/rele/{rele.pk}/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['status'], False)

    def test_rele_detail_delete_view(self):
        client = Client()
        client.login(correo='test@example.com', contrasena='testpassword')

        rele = Rele.objects.create(nombre='Test Rele', topico='test/topic', status=True)

        response = client.delete(f'/rele/{rele.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Puedes agregar más pruebas según sea necesario para otras vistas.

# Ejecutar las pruebas con: python manage.py test



class IotSerializersTest(TestCase):
    def test_relay_serializer(self):
        data = {
            'nombre': 'Test Rele',
            'topico': 'test/topic',
            'status': True
        }

        serializer = RelaySerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_modulo_serializer(self):
        data = {
            'cod_modulo': 1,
            'codigo_usu': 1,
            'nombre': 'Test Modulo',
            'ubicacion': 'Test Location',
            'descripcion': 'Test Description',
            'estado': True
        }

        serializer = ModuloSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_rele_serializer(self):
        data = {
            'is_on': True,
            'cod_registro': 1,
            'cod_modulo': 1,
            'fecha_hora': '2023-01-01T00:00:00Z'
        }

        serializer = ReleSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_aire_serializer(self):
        data = {
            'cod_registro': 1,
            'cod_modulo': 1,
            'fecha_hora': '2023-01-01T00:00:00Z',
            'flujo': 10.5,
            'unidadmedida': 'm3',
            'nivelflujo': 'Alto'
        }

        serializer = AireSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_alert_rele_serializer(self):
        data = {
            'cod_alerta': 1,
            'cod_modulo': 1,
            'cod_registro': 1,
            'fecha_hora': '2023-01-01T00:00:00Z',
            'tipo_alerta': 'Alerta Tipo 1'
        }

        serializer = AlertReleSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_alert_aire_serializer(self):
        data = {
            'cod_alerta': 1,
            'cod_modulo': 1,
            'cod_registro': 1,
            'fecha_hora': '2023-01-01T00:00:00Z',
            'tipo_alerta': 'Alerta Tipo 1'
        }

        serializer = AlertAireSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_mantenimiento_serializer(self):
        data = {
            'cod_mant': 1,
            'codigo_emp': 1,
            'fecha_hora': '2023-01-01T00:00:00Z',
            'tipo_mant': 'Mantenimiento Tipo 1',
            'descripcion': 'Descripción del mantenimiento',
            'realizado': True
        }

        serializer = MantenimientoSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_temporizador_serializer(self):
        data = {
            'cod_temp': 1,
            'codigo_usu': 1,
            'temp_inicio': '2023-01-01T00:00:00Z',
            'temp_fin': '2023-01-02T00:00:00Z',
            'accion': True
        }

        serializer = TemporizadorSerializer(data=data)
        self.assertTrue(serializer.is_valid())

# Ejecutar las pruebas con: python manage.py test
