from rest_framework import viewsets, permissions

from .models import (ItemPortafolio, Servicios, PlanFoto, Cliente,
                     ItemTestimonio, ContactoVenta, Producto, Usuario,
                     Carrito, ListaItem, BlogImagen, Seccion, Cartablog, ImageFolders, ImageConfigPortafolio,
                     ProductoPCarrito, Pedido, PedidoHistorico, ProductosPedido)
from .serializers import (ItemPortafolioSerializer, ServiciosSerializer,
                          PlanFotoSerializer, ClienteSerializer, ItemTestimonioSerializer,
                          ContactoVentaSerializer, ProductoSerializer,
                          UsuarioSerializer, CarritoSerializer, ListaItemSerializer,
                          BlogImagenSerializer, SeccionSerializer, CartablogSerializer, ImageFolderSerializer,
                          ImageConfigPortafolioSerializer, ProductoPCarritoSerializer, PedidoSerializer,
                          PedidoHistoricoSerializer, ProductosPedidoSerializer)


class ImageFolderViewset(viewsets.ModelViewSet):
    queryset = ImageFolders.objects.all()
    serializer_class = ImageFolderSerializer
    permission_classes = [permissions.AllowAny]


class ImageConfigPortafolioViewSet(viewsets.ModelViewSet):
    queryset = ImageConfigPortafolio.objects.all()
    serializer_class = ImageConfigPortafolioSerializer
    permission_classes = [permissions.AllowAny]


class ItemPortafolioViewSet(viewsets.ModelViewSet):
    queryset = ItemPortafolio.objects.all()
    serializer_class = ItemPortafolioSerializer
    permission_classes = [permissions.AllowAny]


class ServiciosViewSet(viewsets.ModelViewSet):
    queryset = Servicios.objects.all()
    serializer_class = ServiciosSerializer
    permission_classes = [permissions.AllowAny]


class PlanFotoViewSet(viewsets.ModelViewSet):
    queryset = PlanFoto.objects.all()
    serializer_class = PlanFotoSerializer
    permission_classes = [permissions.AllowAny]


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [permissions.AllowAny]


class ItemTestimonioViewSet(viewsets.ModelViewSet):
    queryset = ItemTestimonio.objects.all()
    serializer_class = ItemTestimonioSerializer
    permission_classes = [permissions.AllowAny]


class ContactoVentaViewSet(viewsets.ModelViewSet):
    queryset = ContactoVenta.objects.all()
    serializer_class = ContactoVentaSerializer
    permission_classes = [permissions.AllowAny]


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [permissions.AllowAny]


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.AllowAny]


class CarritoViewSet(viewsets.ModelViewSet):
    queryset = Carrito.objects.all()
    serializer_class = CarritoSerializer
    permission_classes = [permissions.AllowAny]


class ListaItemViewSet(viewsets.ModelViewSet):
    queryset = ListaItem.objects.all()
    serializer_class = ListaItemSerializer
    permission_classes = [permissions.AllowAny]


class BlogImagenViewSet(viewsets.ModelViewSet):
    queryset = BlogImagen.objects.all()
    serializer_class = BlogImagenSerializer
    permission_classes = [permissions.AllowAny]


class SeccionViewSet(viewsets.ModelViewSet):
    queryset = Seccion.objects.all()
    serializer_class = SeccionSerializer
    permission_classes = [permissions.AllowAny]


class CartablogViewSet(viewsets.ModelViewSet):
    queryset = Cartablog.objects.all()
    serializer_class = CartablogSerializer
    permission_classes = [permissions.AllowAny]


class ProductoPCarritoViewSet(viewsets.ModelViewSet):
    queryset = ProductoPCarrito.objects.all()
    serializer_class = ProductoPCarritoSerializer
    permission_classes = [permissions.AllowAny]


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    permission_classes = [permissions.AllowAny]


class PedidoHistoricoViewset(viewsets.ModelViewSet):
    queryset = PedidoHistorico.objects.all()
    serializer_class = PedidoHistoricoSerializer
    permission_classes = [permissions.AllowAny]


class ProductosPedidoViewSet(viewsets.ModelViewSet):
    queryset = ProductosPedido.objects.all()
    serializer_class = ProductosPedidoSerializer
    permission_classes = [permissions.AllowAny]
