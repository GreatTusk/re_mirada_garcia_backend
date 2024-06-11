import json

from rest_framework import serializers

from .models import (ImageConfigPortafolio, ItemPortafolio, Servicios, PlanFoto, Cliente,
                     ItemTestimonio, ContactoVenta, Producto, Usuario,
                     Carrito, ListaItem, BlogImagen, Seccion, Cartablog, ImageFolders, ProductoPCarrito)


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


class PlanFotoSerializer(serializers.ModelSerializer):
    incluye = ServiciosSerializer()
    no_incluye = ServiciosSerializer()

    class Meta:
        model = PlanFoto
        fields = ['id', 'titulo', 'precio', 'incluye', 'no_incluye']


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
        fields = ['nombre', 'precio', 'precio_oferta', 'imagen_url']


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
        fields = ['id', 'producto_carrito', 'cantidad']
