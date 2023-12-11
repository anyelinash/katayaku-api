from rest_framework import generics
from django.shortcuts import get_object_or_404
from .models import WhatsAppSettings, Proveedor, Path
from .serializers import WhatsAppSettingsSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import json


# WHATSAPP
class WhatsAppSettingsView(generics.ListCreateAPIView):
    queryset = WhatsAppSettings.objects.all()
    serializer_class = WhatsAppSettingsSerializer

    def get_object(self):
        # Puedes personalizar esto según tus necesidades, por ejemplo, filtrar por usuario
        return WhatsAppSettings.objects.filter(user=self.request.user).first()


class WhatsAppSettingsListView(generics.ListCreateAPIView):
    queryset = WhatsAppSettings.objects.all()
    serializer_class = WhatsAppSettingsSerializer

    def perform_create(self, serializer):
        # Puedes personalizar la lógica de creación aquí, por ejemplo, establecer el usuario
        serializer.save(user=self.request.user)


@csrf_exempt
def send_whatsapp_message(request, id_instance):
    if request.method == 'POST':
        try:
            instance = WhatsAppSettings.objects.get(id_instance=id_instance)
        except WhatsAppSettings.DoesNotExist:
            return JsonResponse({'error': 'WhatsAppSettings not found'}, status=404)

        url = f"https://api.greenapi.com/waInstance{instance.id_instance}/sendMessage/{instance.api_token_instance}"

        try:
            data = json.loads(request.body.decode('utf-8'))
            chat_id = data.get('chatId')
            message = data.get('message')

            payload = {
                'chatId': f'{chat_id}@c.us',
                'message': message
            }

            headers = {
                'Content-Type': 'application/json'
            }

            response = requests.post(url, headers=headers, data=json.dumps(payload))

            return JsonResponse({'status_code': response.status_code, 'response_text': response.text})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON in request body'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)


@csrf_exempt
def send_whatsapp_file(request, id_instance):
    if request.method == 'POST':
        try:
            instance = WhatsAppSettings.objects.get(id_instance=id_instance)
        except WhatsAppSettings.DoesNotExist:
            return JsonResponse({'error': 'WhatsAppSettings not found'}, status=404)

        url = f"https://api.greenapi.com/waInstance{instance.id_instance}/sendFileByUpload/{instance.api_token_instance}"

        try:
            data = json.loads(request.POST.get('data', '{}'))
            chat_id = data.get('chatId', '')
            caption = data.get('caption', '')

            files = request.FILES.getlist('files')
            if not files:
                return JsonResponse({'error': 'No files provided in the request'}, status=400)

            headers = {}

            payload = {
                'chatId': f'{chat_id}@c.us',
                'caption': caption
            }

            response = requests.post(url, headers=headers, data=payload,
                                     files=[('file', (file.name, file.file, file.content_type)) for file in files])

            return JsonResponse({'status_code': response.status_code, 'response_text': response.text})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON in request data'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)


# PROVEEDOR TERCERO FACTILIZA
def consultar_api(request, path_id, proveedor_id, valor):
    path = get_object_or_404(Path, pk=path_id)
    proveedor = get_object_or_404(Proveedor, pk=proveedor_id)

    token = proveedor.token
    url = f'{proveedor.domain}/{path.path}/{valor}'
    headers = {'Authorization': f'Bearer {proveedor.token}'}
    response = requests.get(url, headers=headers)

    # Procesar la respuesta según tus necesidades
    data = response.json() if response.status_code == 200 else {}
    # print(response.status_code)
    # print(response.text)
    # print(proveedor.token)

    return JsonResponse(data)


def listar_paths(request):
    paths = Path.objects.values('id', 'path')  # Obtener los paths como un diccionario
    return JsonResponse(list(paths), safe=False)


def obtener_path_por_id(request, path_id):
    path = get_object_or_404(Path, pk=path_id)
    data = {'id': path.id, 'path': path.path}
    return JsonResponse(data)
