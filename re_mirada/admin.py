from django.contrib import admin

from .models import (ItemPortafolio, Servicios, PlanFoto, Cliente,
                     ItemTestimonio, ImageFolders, Usuario, Carrito, Producto, ProductoPCarrito, Pedido)

# Register your models here.
admin.site.register(PlanFoto)
admin.site.register(Cliente)
admin.site.register(ItemTestimonio)
admin.site.register(ItemPortafolio)
admin.site.register(ImageFolders)
admin.site.register(Servicios)
admin.site.register(Usuario)
admin.site.register(Carrito)
admin.site.register(Producto)
admin.site.register(ProductoPCarrito)
admin.site.register(Pedido)
