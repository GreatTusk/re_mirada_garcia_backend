from django.core.exceptions import ValidationError
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from .models import Usuario, Carrito, ProductoPCarrito, Producto
from .serializers import UsuarioSerializer, ProductoPCarritoSerializer


@api_view(['POST'])
def register_usuario(request):
    id_usu = request.data.get('id')
    nombre = request.data.get('nombre')
    email = request.data.get('email')

    if not id_usu or not nombre or not email:
        return JsonResponse({"error": "ID, nombre, and email are required"}, status=status.HTTP_400_BAD_REQUEST)

    if Usuario.objects.filter(id=id_usu).exists():
        return JsonResponse({"error": "Usuario already exists"}, status=status.HTTP_409_CONFLICT)

    # Create Usuario instance
    usuario = Usuario.objects.create(id=id_usu, nombre=nombre, email=email)

    # Create Carrito instance associated with the Usuario instance
    try:
        carrito = Carrito.objects.create(usuario=usuario, precio_total=0, ahorros=0)
    except ValidationError as e:
        print(e)

    # Serialize and return Usuario instance
    serializer = UsuarioSerializer(usuario)
    return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def carrito_productos(request):
    if request.method == 'GET':
        id_usuario = request.query_params.get('carrito')
        if not id_usuario:
            return JsonResponse({"error": "ID de usuario es requerido"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            carrito_producto = ProductoPCarrito.objects.filter(carrito=id_usuario)
        except Carrito.DoesNotExist:
            return JsonResponse({"error": "Carrito no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        # Serialize the QuerySet
        serializer = ProductoPCarritoSerializer(carrito_producto, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        id_usuario = request.data.get('id')
        id_producto = request.data.get('producto_carrito')
        cantidad_producto = request.data.get('cantidad')

        if not id_usuario or not id_producto:
            return JsonResponse({"error": "ID de usuario y producto son requeridos"},
                                status=status.HTTP_400_BAD_REQUEST)
        try:
            carrito = Carrito.objects.get(usuario=id_usuario)
        except Carrito.DoesNotExist:
            return JsonResponse({"error": "Carrito no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        try:
            producto = Producto.objects.get(id=id_producto)
            ProductoPCarrito.objects.create(carrito=carrito, producto_carrito=producto, cantidad=cantidad_producto)
        except ValidationError as e:
            print(e)
            return JsonResponse({"error": "Producto no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        return JsonResponse({"message": "Producto añadido al carrito"}, status=status.HTTP_201_CREATED)
    elif request.method == 'PUT':
        id_producto_carrito = request.data.get('producto')
        nueva_cantidad = request.data.get('cantidad')

        if not id_producto_carrito or nueva_cantidad is None:
            return JsonResponse({"error": "ID de usuario, producto y cantidad son requeridos"},
                                status=status.HTTP_400_BAD_REQUEST)

        try:
            producto_carrito = ProductoPCarrito.objects.get(id=id_producto_carrito)
        except ProductoPCarrito.DoesNotExist:
            return JsonResponse({"error": "Producto en carrito no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        producto_carrito.cantidad = nueva_cantidad
        producto_carrito.save()
        # Serialize the updated ProductoPCarrito object
        serializer = ProductoPCarritoSerializer(producto_carrito)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        id_producto_carrito = request.data.get('producto')
        if not id_producto_carrito:
            return JsonResponse({"error": "producto es requeridos"},
                                status=status.HTTP_400_BAD_REQUEST)
        try:
            producto_carrito = ProductoPCarrito.objects.get(id=id_producto_carrito)
        except ProductoPCarrito.DoesNotExist:
            return JsonResponse({"error": "Producto en carrito no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        producto_carrito.delete()

        return JsonResponse({"message": "Producto eliminado del carrito"}, status=status.HTTP_200_OK)
