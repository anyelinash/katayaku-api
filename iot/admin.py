from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Modulo)
admin.site.register(RegistrosRele)
admin.site.register(RegistrosAgua)
admin.site.register(RegistrosUltrasonico)
admin.site.register(RegistrosAire)
admin.site.register(AlertasRele)
admin.site.register(AlertasAgua)
admin.site.register(AlertasSonico)
admin.site.register(AlertasAire)
admin.site.register(Mantenimientos)
admin.site.register(Temporizadores)
admin.site.register(Rele)