from django.shortcuts import render
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

channel_layer = get_channel_layer()


async def some_view(request):
    # ...
    # Algo en tu vista
    # ...

    # Enviar un mensaje a través de websockets
    async_to_sync(channel_layer.group_send)(
        'nombre_del_grupo',
        {
            'type': 'chat.message',
            'message': 'Hola desde el servidor!',
        }
    )
    # ...
