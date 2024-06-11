from rest_framework import routers
from django.urls import path, include
from .api import (ItemPortafolioViewSet, ServiciosViewSet, PlanFotoViewSet, ClienteViewSet,
                  ItemTestimonioViewSet, ContactoVentaViewSet, ProductoViewSet, ProductoCarritoViewSet,
                  UsuarioViewSet, CarritoViewSet, ListaItemViewSet, BlogImagenViewSet, SeccionViewSet,
                  CartablogViewSet, ImageFolderViewset, ImageConfigPortafolioViewSet, ProductoPCarritoViewSet)
from .views import register_usuario

router = routers.DefaultRouter()
router.register('itemportafolio', ItemPortafolioViewSet)
router.register('servicios', ServiciosViewSet)
router.register('planfoto', PlanFotoViewSet)
router.register('cliente', ClienteViewSet)
router.register('itemtestimonio', ItemTestimonioViewSet)
router.register('contactoventa', ContactoVentaViewSet)
router.register('producto', ProductoViewSet)
router.register('productocarrito', ProductoCarritoViewSet)
router.register('usuario', UsuarioViewSet)
router.register('carrito', CarritoViewSet)
router.register('listaitem', ListaItemViewSet)
router.register('blogimagen', BlogImagenViewSet)
router.register('seccion', SeccionViewSet)
router.register('cartablog', CartablogViewSet)
router.register('imagefolders', ImageFolderViewset)
router.register('imageconfigportafolio', ImageConfigPortafolioViewSet)
router.register('productopcarrito', ProductoPCarritoViewSet)

urlpatterns = router.urls
urlpatterns += [
    path('register_usuario/', register_usuario),
]
