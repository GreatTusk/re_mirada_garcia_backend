import json

from django.db import models


class ImageFolders(models.Model):
    folder = models.CharField(max_length=255)


class ImageConfigPortafolio(models.Model):
    image_folder = models.ForeignKey(ImageFolders, on_delete=models.CASCADE)
    width = models.IntegerField()
    height = models.IntegerField()


class ItemPortafolio(models.Model):
    images_config = models.ForeignKey(ImageConfigPortafolio, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()


class Servicios(models.Model):
    servicios = models.TextField()

    def set_servicios(self, servicios_list):
        self.servicios = json.dumps(servicios_list)

    def get_servicios(self):
        return json.loads(self.servicios)


class PlanFoto(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    titulo = models.CharField(max_length=255)
    precio = models.IntegerField()
    incluye = models.ForeignKey(Servicios, related_name='incluye', on_delete=models.CASCADE)
    no_incluye = models.ForeignKey(Servicios, related_name='no_incluye', on_delete=models.CASCADE)


class Cliente(models.Model):
    nombre = models.CharField(max_length=255)
    image_url = models.URLField()
    ocupacion = models.CharField(max_length=255)


class ItemTestimonio(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    testimonio = models.TextField()


class ContactoVenta(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    email = models.EmailField()
    nombre = models.CharField(max_length=255)
    fono = models.CharField(max_length=255)
    consulta = models.TextField()
    boletin = models.TextField()


class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    precio = models.IntegerField()
    imagen_url = models.CharField(max_length=255)
    precio_oferta = models.IntegerField(null=True, blank=True)


class Usuario(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    nombre = models.CharField(max_length=255)
    email = models.EmailField()


class Carrito(models.Model):
    usuario = models.OneToOneField(Usuario, primary_key=True, on_delete=models.CASCADE)
    precio_total = models.IntegerField()
    ahorros = models.IntegerField()


class ProductoPCarrito(models.Model):
    # carrito = id_usuario
    carrito = models.ForeignKey(Carrito, default=None, on_delete=models.CASCADE)
    producto_carrito = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()


class ListaItem(models.Model):
    titulo = models.CharField(max_length=255)
    texto = models.TextField()


class BlogImagen(models.Model):
    src = models.URLField()
    alt = models.CharField(max_length=255)
    width = models.IntegerField()
    height = models.IntegerField()
    class_name = models.CharField(max_length=255)
    caption = models.CharField(max_length=255)


class Seccion(models.Model):
    titulo = models.CharField(max_length=255)
    bajada_texto = models.TextField(null=True, blank=True)
    parrafos = models.TextField(null=True, blank=True)
    imagen = models.ForeignKey(BlogImagen, null=True, blank=True, on_delete=models.CASCADE)
    lista = models.ManyToManyField(ListaItem)


class Cartablog(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    titulo = models.CharField(max_length=255)
    bajada_titulo = models.CharField(max_length=255)
    secciones = models.ManyToManyField(Seccion)
    fechapub = models.DateField()
    tag = models.CharField(max_length=255)
    cita = models.TextField(null=True, blank=True)
