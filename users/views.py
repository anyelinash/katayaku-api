from .models import Usuario, Empresa, Reporte
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from .serializer import *
from django.contrib.auth.decorators import login_required
# from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class IndexView(APIView):

    def get(self, request):
        context = {'mensaje': 'servidor activo'}
        return Response(context)


# Empresa
class EmpView(APIView):

    def get(self, request):
        dataEmp = Empresa.objects.all()
        serEmp = EmpresaSerializer(dataEmp, many=True)
        return Response(serEmp.data)

    def post(self, request):
        serEmp = EmpresaSerializer(data=request.data)
        serEmp.is_valid(raise_exception=True)
        serEmp.save()

        return Response(serEmp.data)


class EmpDetailView(APIView):

    def get(self, request, pk):
        dataEmp = Empresa.objects.get(codigo_emp=pk)
        serEmp = EmpresaSerializer(dataEmp)
        return Response(serEmp.data)

    def put(self, request, pk):
        dataEmp = Empresa.objects.get(codigo_emp=pk)
        serEmp = EmpresaSerializer(dataEmp, data=request.data)
        serEmp.is_valid(raise_exception=True)
        serEmp.save()
        return Response(serEmp.data)

    def delete(self, request, pk):
        dataEmp = Empresa.objects.get(codigo_emp=pk)
        serEmp = EmpresaSerializer(dataEmp)
        dataEmp.delete()
        return Response(serEmp.data)


# Usuario

class UsuarioRegistrationView(APIView):
    def post(self, request):
        serializer = UsuarioRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  # This calls Usuario.objects.create_user
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'user': UsuarioSerializer(user).data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsuarioLoginView(APIView):
    def post(self, request):
        serializer = UsuarioLoginSerializer(data=request.data)
        if serializer.is_valid():
            correo = serializer.validated_data['correo']
            contrasena = serializer.validated_data['contrasena']

            # Authenticate user
            usuario = authenticate(request, correo=correo, contrasena=contrasena)
            if usuario:
                # Login user
                login(request, usuario)

                # Assuming you are using the `Token` model from DRF for token authentication
                token, _ = Token.objects.get_or_create(user=usuario)

                return Response({'token': token.key, 'user': UsuarioSerializer(usuario).data}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsuListView(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    @authentication_classes([TokenAuthentication, SessionAuthentication])
    @permission_classes([permissions.IsAuthenticated])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @authentication_classes([TokenAuthentication, SessionAuthentication])
    @permission_classes([permissions.IsAuthenticated])
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class UsuDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    @authentication_classes([TokenAuthentication, SessionAuthentication])
    @permission_classes([permissions.IsAuthenticated])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @authentication_classes([TokenAuthentication, SessionAuthentication])
    @permission_classes([permissions.IsAuthenticated])
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @authentication_classes([TokenAuthentication, SessionAuthentication])
    @permission_classes([permissions.IsAuthenticated])
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class UsuarioLogoutView(APIView):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Aquí puedes realizar cualquier lógica de logout necesaria
        # Por ejemplo, invalidar tokens, eliminar sesiones, etc.
        request.auth.delete()  # Eliminar el token de autenticación (si estás utilizando tokens)

        # Otros pasos de logout según tu implementación

        return Response({'detail': 'Logout exitoso'}, status=status.HTTP_200_OK)


# Reportes de usuarios
class RepView(APIView):

    def get(self, request):
        dataRep = Reporte.objects.all()
        serRep = ReporteSerializer(dataRep, many=True)
        return Response(serRep.data)

    def post(self, request):
        serRep = ReporteSerializer(data=request.data)
        serRep.is_valid(raise_exception=True)
        serRep.save()
        return Response(serRep.data)


class RepDetailView(APIView):
    def get(self, request, pk):
        dataRep = Reporte.objects.get(codigo_rep=pk)
        serRep = ReporteSerializer(dataRep)
        return Response(serRep.data)

    def put(self, request, pk):
        dataRep = Reporte.objects.get(codigo_rep=pk)
        serRep = ReporteSerializer(dataRep, data=request.data)
        serRep.is_valid(raise_exception=True)
        serRep.save()
        return Response(serRep.data)

    def delete(self, request, pk):
        dataRep = Reporte.objects.get(codigo_rep=pk)
        serRep = ReporteSerializer(dataRep)
        dataRep.delete()
        return Response(serRep.data)
