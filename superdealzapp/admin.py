from django.contrib import admin
from .models import *


class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ('highlighted',)

class PrecioAdmin(admin.ModelAdmin):
    readonly_fields = ('highlighted',)

admin.site.register(Producto)
admin.site.register(Precio)
admin.site.register(Supermercado)
admin.site.register(Categoria)
admin.site.register(Error)

