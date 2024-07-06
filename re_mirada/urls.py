from django.urls import path
from rest_framework import routers

from .api import (ItemPortafolioViewSet, ServiciosViewSet, PlanFotoViewSet, ClienteViewSet,
                  ItemTestimonioViewSet, ContactoVentaViewSet, ProductoViewSet,
                  UsuarioViewSet, CarritoViewSet, ListaItemViewSet, BlogImagenViewSet, SeccionViewSet,
                  CartablogViewSet, ImageFolderViewset, ImageConfigPortafolioViewSet, ProductoPCarritoViewSet,
                  PedidoViewSet, PedidoHistoricoViewset, ProductosPedidoViewSet)
from .views import register_usuario, carrito_productos, carrito_pedido, productos_pedido, get_total_recaudado, \
    get_total_pedidos, get_total_usuarios, get_recaudado_por_mes, get_info_productos, get_pedido_detalle, get_user_ids

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
    path('productos_pedido/', productos_pedido),
    path('get_total_recaudado/', get_total_recaudado),
    path('get_total_pedidos/', get_total_pedidos),
    path('get_total_usuarios/', get_total_usuarios),
    path('get_recaudado_por_mes/', get_recaudado_por_mes),
    path('get_info_productos/', get_info_productos),
    path('get_pedido_detalle/', get_pedido_detalle),
    path('get_user_ids/', get_user_ids)
]
