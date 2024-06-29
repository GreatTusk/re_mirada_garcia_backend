from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from .models import (ItemPortafolio, Servicios, PlanFoto, Cliente,
                     ItemTestimonio, ContactoVenta, Producto, Usuario,
                     Carrito, ListaItem, BlogImagen, Seccion, Cartablog, ImageFolders, ImageConfigPortafolio,
                     ProductoPCarrito, Pedido)
from .serializers import (ItemPortafolioSerializer, ServiciosSerializer,
                          PlanFotoSerializer, ClienteSerializer, ItemTestimonioSerializer,
                          ContactoVentaSerializer, ProductoSerializer,
                          UsuarioSerializer, CarritoSerializer, ListaItemSerializer,
                          BlogImagenSerializer, SeccionSerializer, CartablogSerializer, ImageFolderSerializer,
                          ImageConfigPortafolioSerializer, ProductoPCarritoSerializer, PedidoSerializer)


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

    # @action(detail=False, methods=['post'])
    # def register_usuario(self, request):
    #     print("register_usuario called")
    #     id_usu = request.data.get('id')
    #     nombre = request.data.get('nombre')
    #     email = request.data.get('email')
    #
    #     if not id_usu or not nombre or not email:
    #         return Response({"error": "ID, nombre, and email are required"}, status=status.HTTP_400_BAD_REQUEST)
    #
    #     if Usuario.objects.filter(id=id_usu).exists():
    #         return Response({"error": "Usuario already exists"}, status=status.HTTP_409_CONFLICT)
    #
    #     # Create Usuario instance
    #     usuario = Usuario.objects.create(id=id_usu, nombre=nombre, email=email)
    #
    #     # Create Carrito instance associated with the Usuario instance
    #     try:
    #         carrito = Carrito.objects.create(usuario=usuario, precio_total=0, ahorros=0)
    #         print(carrito)
    #     except ValidationError as e:
    #         print(e)
    #
    #     # Serialize and return Usuario instance
    #     serializer = UsuarioSerializer(usuario)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)


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
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    permission_classes = [permissions.AllowAny]
