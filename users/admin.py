from django.contrib import admin
from .models import Empresa, Usuario, Reporte

# Register your models here.
admin.site.register(Empresa)
admin.site.register(Usuario)
admin.site.register(Reporte)

