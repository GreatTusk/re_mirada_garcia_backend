import json

from rest_framework import serializers

from .models import (ImageConfigPortafolio, ItemPortafolio, Servicios, PlanFoto, Cliente,
                     ItemTestimonio, ContactoVenta, Producto, Usuario,
                     Carrito, ListaItem, BlogImagen, Seccion, Cartablog, ImageFolders, ProductoPCarrito, Pedido,
                     PedidoHistorico, ProductosPedido)


class ImageFolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageFolders
        fields = ['folder']


class ImageConfigPortafolioSerializer(serializers.ModelSerializer):
    image_folder = ImageFolderSerializer(read_only=True)

    class Meta:
        model = ImageConfigPortafolio
        fields = ['id', 'image_folder', 'width', 'height']


class ItemPortafolioSerializer(serializers.ModelSerializer):
    images_config = ImageConfigPortafolioSerializer()

    class Meta:
        model = ItemPortafolio
        fields = ['images_config', 'titulo', 'descripcion']

    def create(self, validated_data):
        images_config_data = validated_data.pop('images_config')
        item_portafolio = ItemPortafolio.objects.create(**validated_data)
        ImageConfigPortafolio.objects.create(item_portafolio=item_portafolio, **images_config_data)
        return item_portafolio


class ServiciosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicios
        fields = ['servicios']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['servicios'] = json.loads(representation['servicios'])
        return representation


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'


class ItemTestimonioSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer()

    class Meta:
        model = ItemTestimonio
        fields = '__all__'


class ContactoVentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactoVenta
        fields = '__all__'


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'precio', 'precio_oferta', 'imagen_url']


class PlanFotoSerializer(serializers.ModelSerializer):
    incluye = ServiciosSerializer()
    no_incluye = ServiciosSerializer()
    id_producto = ProductoSerializer()

    class Meta:
        model = PlanFoto
        fields = ['id_producto', 'incluye', 'no_incluye']


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'


class CarritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrito
        fields = '__all__'


class ListaItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListaItem
        fields = '__all__'


class BlogImagenSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogImagen
        fields = '__all__'


class SeccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seccion
        fields = '__all__'


class CartablogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cartablog
        fields = '__all__'


class ProductoPCarritoSerializer(serializers.ModelSerializer):
    producto_carrito = ProductoSerializer()

    class Meta:
        model = ProductoPCarrito
        fields = ['id', 'producto_carrito', 'cantidad', 'carrito']


class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'


class PedidoHistoricoSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField()

    class Meta:
        model = PedidoHistorico
        fields = ['id_pedido', 'usuario', 'direccion', 'region', 'comuna', 'descripcion', 'fecha', 'metodo_pago',
                  'nombre_empresa', 'rut_empresa', 'first_name', 'last_name', 'email', 'phone_number', 'fecha_creacion',
                  'total']

    def get_total(self, obj):
        productos_pedido = ProductosPedido.objects.filter(pedido=obj)
        return sum([producto.precio_total for producto in productos_pedido])


class ProductosPedidoSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer()

    class Meta:
        model = ProductosPedido
        fields = ['producto', 'cantidad', 'precio_total']
