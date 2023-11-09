from .models import Usuario, Empresa
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import EmpresaSerializer, UsuarioSerializer

class IndexView(APIView):
    
    def get(self,request):
        context = {'mensaje':'servidor activo'}
        return Response(context)
    
#Empresa
class EmpView(APIView):

    def get(self,request):
        dataEmp = Empresa.objects.all()
        serEmp = EmpresaSerializer(dataEmp,many=True)
        return Response(serEmp.data)
    
    def post(self,request):
        serEmp = EmpresaSerializer(data=request.data)
        serEmp.is_valid(raise_exception=True)
        serEmp.save()
        
        return Response(serEmp.data)
    
class EmpDetailView(APIView):
    
    def get(self,request,pk):
        dataEmp = Empresa.objects.get(codigo_emp=pk)
        serEmp = EmpresaSerializer(dataEmp)
        return Response(serEmp.data)
    
    def put(self,request,pk):
        dataEmp = Empresa.objects.get(codigo_emp=pk)
        serEmp = EmpresaSerializer(dataEmp,data=request.data)
        serEmp.is_valid(raise_exception=True)
        serEmp.save()
        return Response(serEmp.data)
    
    def delete(self,request,pk):
        dataEmp = Empresa.objects.get(codigo_emp=pk)
        serEmp = EmpresaSerializer(dataEmp)
        dataEmp.delete()
        return Response(serEmp.data)

#Usuario
class UsuView(APIView):

    def get(self,request):
        dataUsu = Usuario.objects.all()
        serUsu = UsuarioSerializer(dataUsu,many=True)
        return Response(serUsu.data)
    
    def post(self,request):
        serUsu = UsuarioSerializer(data=request.data)
        serUsu.is_valid(raise_exception=True)
        serUsu.save()
        return Response(serUsu.data)
    
class UsuDetailView(APIView):
    def get(self,request,pk):
        dataUsu = Usuario.objects.get(codigo_usu=pk)
        serUsu = UsuarioSerializer(dataUsu)
        return Response(serUsu.data)
    
    def put(self,request,pk):
        dataUsu = Usuario.objects.get(codigo_usu=pk)
        serUsu = UsuarioSerializer(dataUsu,data=request.data)
        serUsu.is_valid(raise_exception=True)
        serUsu.save()
        return Response(serUsu.data)
    
    def delete(self,request,pk):
        dataUsu = Usuario.objects.get(codigo_usu=pk)
        serUsu = UsuarioSerializer(dataUsu)
        dataUsu.delete()
        return Response(serUsu.data)
    
class UsuariosPorEmpresaView(APIView):
    def get(self, request, cod_emp, format=None):
        try:
            usuarios = Usuario.objects.filter(codigo_emp=cod_emp)
            usuario_data = [{'codigo_usu': usuario.codigo_usu, 'nombre': usuario.nombre} for usuario in usuarios]
            return Response(usuario_data, status=status.HTTP_200_OK)
        except Usuario.DoesNotExist:
            return Response({'error': 'No se encontraron usuarios para la empresa con el código proporcionado'}, status=status.HTTP_404_NOT_FOUND)