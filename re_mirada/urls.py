from rest_framework import routers
from django.urls import path, include
from .api import (ItemPortafolioViewSet, ServiciosViewSet, PlanFotoViewSet, ClienteViewSet,
                  ItemTestimonioViewSet, ContactoVentaViewSet, ProductoViewSet,
                  UsuarioViewSet, CarritoViewSet, ListaItemViewSet, BlogImagenViewSet, SeccionViewSet,
                  CartablogViewSet, ImageFolderViewset, ImageConfigPortafolioViewSet, ProductoPCarritoViewSet,
                  PedidoViewSet, PedidoHistoricoViewset, ProductosPedidoViewSet)
from .views import register_usuario, carrito_productos, carrito_pedido

router = routers.DefaultRouter()
router.register('itemportafolio', ItemPortafolioViewSet)
router.register('servicios', ServiciosViewSet)
router.register('planfoto', PlanFotoViewSet)
router.register('cliente', ClienteViewSet)
router.register('itemtestimonio', ItemTestimonioViewSet)
router.register('contactoventa', ContactoVentaViewSet)
router.register('producto', ProductoViewSet)
router.register('usuario', UsuarioViewSet)
router.register('carrito', CarritoViewSet)
router.register('listaitem', ListaItemViewSet)
router.register('blogimagen', BlogImagenViewSet)
router.register('seccion', SeccionViewSet)
router.register('cartablog', CartablogViewSet)
router.register('imagefolders', ImageFolderViewset)
router.register('imageconfigportafolio', ImageConfigPortafolioViewSet)
router.register('productopcarrito', ProductoPCarritoViewSet)
router.register('pedido', PedidoViewSet)
router.register('pedidohistorico', PedidoHistoricoViewset)
router.register('productospedido', ProductosPedidoViewSet)

urlpatterns = router.urls
urlpatterns += [
    path('register_usuario/', register_usuario),
    path('carrito_productos/', carrito_productos),
    path('carrito_pedido/', carrito_pedido),
]
