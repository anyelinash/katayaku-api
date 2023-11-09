from .models import *
from .serializer import ModuloSerializer, ReleSerializer, AguaSerializer, SonicoSerializer, AireSerializer, AlertReleSerializer, AlertAguaSerializer, AlertSonicoSerializer, AlertAireSerializer, MantenimientoSerializer, TemporizadorSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class IndexView(APIView):
    
    def get(self,request):
        context = {'mensaje':'servidor activo'}
        return Response(context)
    
# Módulos - General
class ModsView(APIView):

    def get(self,request):
        dataMods = Modulo.objects.all()
        serMods = ModuloSerializer(dataMods,many=True)
        return Response(serMods.data)
    
    def post(self,request):
        serMods = ModuloSerializer(data=request.data)
        serMods.is_valid(raise_exception=True)
        serMods.save()
        
        return Response(serMods.data)
    
class ModsDetailView(APIView):
    def get(self,request,pk):
        dataMods = Modulo.objects.get(cod_modulo=pk)
        serMods = ModuloSerializer(dataMods)
        return Response(serMods.data)
    
    def put(self,request,pk):
        dataMods = Modulo.objects.get(cod_modulo=pk)
        serMods = ModuloSerializer(dataMods,data=request.data)
        serMods.is_valid(raise_exception=True)
        serMods.save()
        return Response(serMods.data)
    
    def delete(self,request,pk):
        dataMods = Modulo.objects.get(cod_modulo=pk)
        serMods = ModuloSerializer(dataMods)
        dataMods.delete()
        return Response(serMods.data)

#Registros
#Relé
class ReleView(APIView):
    def get(self,request):
        dataRele = RegistrosRele.objects.all()
        serRele = ReleSerializer(dataRele,many=True)
        return Response(serRele.data)
     
    def post(self,request):
        serRele = ReleSerializer(data=request.data)
        serRele.is_valid(raise_exception=True)
        serRele.save()
        return Response(serRele.data)
    
class ReleDetailView(APIView):
    def get(self,request,pk):
        dataRele = RegistrosRele.objects.get(cod_registro=pk)
        serRele = ReleSerializer(dataRele)
        return Response(serRele.data)
    
    def put(self,request,pk):
        dataRele = RegistrosRele.objects.get(cod_registro=pk)
        serRele = ReleSerializer(dataRele,data=request.data)
        serRele.is_valid(raise_exception=True)
        serRele.save()
        return Response(serRele.data)
    
    def delete(self,request,pk):
        dataRele = RegistrosRele.objects.get(cod_registro=pk)
        serRele = ReleSerializer(dataRele)
        dataRele.delete()
        return Response(serRele.data)
    
#Sensor de flujo de agua
class AguaView(APIView):
    def get(self,request):
        dataAg = RegistrosAgua.objects.all()
        serAg = AguaSerializer(dataAg,many=True)
        return Response(serAg.data)
     
    def post(self,request):
        serAg = AguaSerializer(data=request.data)
        serAg.is_valid(raise_exception=True)
        serAg.save()
        return Response(serAg.data)
    
class AguaDetailView(APIView):
    def get(self,request,pk):
        dataAg = RegistrosAgua.objects.get(cod_registro=pk)
        serAg = AguaSerializer(dataAg)
        return Response(serAg.data)
    
    def put(self,request,pk):
        dataAg = RegistrosAgua.objects.get(cod_registro=pk)
        serAg = AguaSerializer(dataAg,data=request.data)
        serAg.is_valid(raise_exception=True)
        serAg.save()
        return Response(serAg.data)
    
    def delete(self,request,pk):
        dataAg = RegistrosAgua.objects.get(cod_registro=pk)
        serAg = AguaSerializer(dataAg)
        dataAg.delete()
        return Response(serAg.data)
    
#Sensor ultrasónico
class SonicView(APIView):
    def get(self,request):
        dataUs = RegistrosUltrasonico.objects.all()
        serUs = SonicoSerializer(dataUs,many=True)
        return Response(serUs.data)
     
    def post(self,request):
        serUs = SonicoSerializer(data=request.data)
        serUs.is_valid(raise_exception=True)
        serUs.save()
        return Response(serUs.data)
    
class SonicDetailView(APIView):
    def get(self,request,pk):
        dataUs = RegistrosUltrasonico.objects.get(cod_registro=pk)
        serUs = SonicoSerializer(dataUs)
        return Response(serUs.data)
    
    def put(self,request,pk):
        dataUs = RegistrosUltrasonico.objects.get(cod_registro=pk)
        serUs = SonicoSerializer(dataUs,data=request.data)
        serUs.is_valid(raise_exception=True)
        serUs.save()
        return Response(serUs.data)
    
    def delete(self,request,pk):
        dataUs = RegistrosUltrasonico.objects.get(cod_registro=pk)
        serUs = SonicoSerializer(dataUs)
        dataUs.delete()
        return Response(serUs.data)
    
#Sensor de calidad de aire
class AireView(APIView):
    def get(self,request):
        dataAi = RegistrosAire.objects.all()
        serAi = AireSerializer(dataAi,many=True)
        return Response(serAi.data)
     
    def post(self,request):
        serAi = AireSerializer(data=request.data)
        serAi.is_valid(raise_exception=True)
        serAi.save()
        return Response(serAi.data)
    
class AireDetailView(APIView):
    def get(self,request,pk):
        dataAi = RegistrosAire.objects.get(cod_registro=pk)
        serAi = AireSerializer(dataAi)
        return Response(serAi.data)
    
    def put(self,request,pk):
        dataAi = RegistrosAire.objects.get(cod_registro=pk)
        serAi = AireSerializer(dataAi,data=request.data)
        serAi.is_valid(raise_exception=True)
        serAi.save()
        return Response(serAi.data)
    
    def delete(self,request,pk):
        dataAi = RegistrosAire.objects.get(cod_registro=pk)
        serAi = AireSerializer(dataAi)
        dataAi.delete()
        return Response(serAi.data)
    
# Alertas
# Alertas Rele
class AltReleView(APIView):
    def get(self,request):
        dataAre = AlertasRele.objects.all()
        serAre = AlertReleSerializer(dataAre,many=True)
        return Response(serAre.data)
     
    def post(self,request):
        serAre = AlertReleSerializer(data=request.data)
        serAre.is_valid(raise_exception=True)
        serAre.save()
        return Response(serAre.data)
    
class AltReleDetailView(APIView):
    def get(self,request,pk):
        dataAre = AlertasRele.objects.get(cod_alerta=pk)
        serAre = AlertReleSerializer(dataAre)
        return Response(serAre.data)
    
    def put(self,request,pk):
        dataAre = AlertasRele.objects.get(cod_alerta=pk)
        serAre = AlertReleSerializer(dataAre,data=request.data)
        serAre.is_valid(raise_exception=True)
        serAre.save()
        return Response(serAre.data)
    
    def delete(self,request,pk):
        dataAre = AlertasRele.objects.get(cod_alerta=pk)
        serAre = AlertReleSerializer(dataAre)
        dataAre.delete()
        return Response(serAre.data)
    
# Alertas Sensor de flujo de agua
class AltAguaView(APIView):
    def get(self,request):
        dataAgu = AlertasAgua.objects.all()
        serAgu = AlertAguaSerializer(dataAgu,many=True)
        return Response(serAgu.data)
     
    def post(self,request):
        serAgu = AlertAguaSerializer(data=request.data)
        serAgu.is_valid(raise_exception=True)
        serAgu.save()
        return Response(serAgu.data)
    
class AltAguaDetailView(APIView):
    def get(self,request,pk):
        dataAgu = AlertasAgua.objects.get(cod_alerta=pk)
        serAgu = AlertAguaSerializer(dataAgu)
        return Response(serAgu.data)
    
    def put(self,request,pk):
        dataAgu = AlertasAgua.objects.get(cod_alerta=pk)
        serAgu = AlertAguaSerializer(dataAgu,data=request.data)
        serAgu.is_valid(raise_exception=True)
        serAgu.save()
        return Response(serAgu.data)
    
    def delete(self,request,pk):
        dataAgu = AlertasAgua.objects.get(cod_alerta=pk)
        serAgu = AlertAguaSerializer(dataAgu)
        dataAgu.delete()
        return Response(serAgu.data)
    
# Alertas Sensor ultrasónico
class AltSonicView(APIView):
    def get(self,request):
        dataAso = AlertasSonico.objects.all()
        serAso = AlertSonicoSerializer(dataAso,many=True)
        return Response(serAso.data)
     
    def post(self,request):
        serAso = AlertSonicoSerializer(data=request.data)
        serAso.is_valid(raise_exception=True)
        serAso.save()
        return Response(serAso.data)
    
class AltSonicDetailView(APIView):
    def get(self,request,pk):
        dataAso = AlertasSonico.objects.get(cod_alerta=pk)
        serAso = AlertSonicoSerializer(dataAso)
        return Response(serAso.data)
    
    def put(self,request,pk):
        dataAso = AlertasSonico.objects.get(cod_alerta=pk)
        serAso = AlertSonicoSerializer(dataAso,data=request.data)
        serAso.is_valid(raise_exception=True)
        serAso.save()
        return Response(serAso.data)
    
    def delete(self,request,pk):
        dataAso = AlertasSonico.objects.get(cod_alerta=pk)
        serAso = AlertSonicoSerializer(dataAso)
        dataAso.delete()
        return Response(serAso.data)
    
# Alertas Sensor de calidad de aire
class AltAireView(APIView):
    def get(self,request):
        dataAlre = AlertasAire.objects.all()
        serAlre = AlertAireSerializer(dataAlre,many=True)
        return Response(serAlre.data)
     
    def post(self,request):
        serAlre = AlertAireSerializer(data=request.data)
        serAlre.is_valid(raise_exception=True)
        serAlre.save()
        return Response(serAlre.data)
    
class AltAireDetailView(APIView):
    def get(self,request,pk):
        dataAlre = AlertasAire.objects.get(cod_alerta=pk)
        serAlre = AlertAireSerializer(dataAlre)
        return Response(serAlre.data)
    
    def put(self,request,pk):
        dataAlre = AlertasAire.objects.get(cod_alerta=pk)
        serAlre = AlertAireSerializer(dataAlre,data=request.data)
        serAlre.is_valid(raise_exception=True)
        serAlre.save()
        return Response(serAlre.data)
    
    def delete(self,request,pk):
        dataAlre = AlertasAire.objects.get(cod_alerta=pk)
        serAlre = AlertAireSerializer(dataAlre)
        dataAlre.delete()
        return Response(serAlre.data)
    
# mantenimientos
class MantemimientoView(APIView):
    def get(self,request):
        dataMant = Mantenimientos.objects.all()
        serMant = MantenimientoSerializer(dataMant,many=True)
        return Response(serMant.data)
     
    def post(self,request):
        serMant = MantenimientoSerializer(data=request.data)
        serMant.is_valid(raise_exception=True)
        serMant.save()
        return Response(serMant.data)
    
class MantemimientoDetailView(APIView):
    def get(self,request,pk):
        dataMant = Mantenimientos.objects.get(cod_mant=pk)
        serMant = MantenimientoSerializer(dataMant)
        return Response(serMant.data)
    
    def put(self,request,pk):
        dataMant = Mantenimientos.objects.get(cod_mant=pk)
        serMant = MantenimientoSerializer(dataMant,data=request.data)
        serMant.is_valid(raise_exception=True)
        serMant.save()
        return Response(serMant.data)
    
    def delete(self,request,pk):
        dataMant = Mantenimientos.objects.get(cod_mant=pk)
        serMant = MantenimientoSerializer(dataMant)
        dataMant.delete()
        return Response(serMant.data)

# temporizadores
class TemporizadoresView(APIView):
    def get(self,request):
        dataTemp = Temporizadores.objects.all()
        serTemp = TemporizadorSerializer(dataTemp,many=True)
        return Response(serTemp.data)
     
    def post(self,request):
        serTemp = TemporizadorSerializer(data=request.data)
        serTemp.is_valid(raise_exception=True)
        serTemp.save()
        return Response(serTemp.data)
    
class TemporizadoresDetailView(APIView):
    def get(self,request,pk):
        dataTemp = Temporizadores.objects.get(cod_temp=pk)
        serTemp = TemporizadorSerializer(dataTemp)
        return Response(serTemp.data)
    
    def put(self,request,pk):
        dataTemp = Temporizadores.objects.get(cod_temp=pk)
        serTemp = TemporizadorSerializer(dataTemp,data=request.data)
        serTemp.is_valid(raise_exception=True)
        serTemp.save()
        return Response(serTemp.data)
    
    def delete(self,request,pk):
        dataTemp = Temporizadores.objects.get(cod_temp=pk)
        serTemp = TemporizadorSerializer(dataTemp)
        dataTemp.delete()
        return Response(serTemp.data)
