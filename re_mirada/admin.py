from django.contrib import admin
from .models import (ItemPortafolio, Servicios, PlanFoto, Cliente,
                     ItemTestimonio, ImageFolders, Usuario, Carrito)

# Register your models here.
admin.site.register(PlanFoto)
admin.site.register(Cliente)
admin.site.register(ItemTestimonio)
admin.site.register(ItemPortafolio)
admin.site.register(ImageFolders)
admin.site.register(Servicios)
admin.site.register(Usuario)
admin.site.register(Carrito)
