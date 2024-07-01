import uuid

from django.core.exceptions import ValidationError
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from .models import Usuario, Carrito, ProductoPCarrito, Producto, Pedido, PedidoHistorico, ProductosPedido
from .serializers import UsuarioSerializer, ProductoPCarritoSerializer, PedidoHistoricoSerializer


@api_view(['POST', 'PUT'])
def register_usuario(request):
    if request.method == 'POST':
        id_usu = request.data.get('id')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        email = request.data.get('email')
        phone_number = request.data.get('phone_number')

        if not id_usu or not first_name or not email:
            return JsonResponse({"error": "ID, nombre, and email are required"}, status=status.HTTP_400_BAD_REQUEST)

        if Usuario.objects.filter(id=id_usu).exists():
            return JsonResponse({"error": "Usuario already exists"}, status=status.HTTP_409_CONFLICT)

        # Create Usuario instance
        usuario = Usuario.objects.create(id=id_usu, first_name=first_name, last_name=last_name, email=email,
                                         phone_number=phone_number)

        # Create Carrito instance associated with the Usuario instance
        try:
            carrito = Carrito.objects.create(usuario=usuario, precio_total=0, ahorros=0)
        except ValidationError as e:
            print(e)

        # Serialize and return Usuario instance
        serializer = UsuarioSerializer(usuario)
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'PUT':
        id_usu = request.data.get('id')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        email = request.data.get('email')
        phone_number = request.data.get('phone_number')

        if not id_usu or not first_name or not email or not last_name or not phone_number:
            return JsonResponse({"error": "ID, nombre, and email are required"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            usuario = Usuario.objects.get(id=id_usu)
        except Usuario.DoesNotExist:
            return JsonResponse({"error": "Usuario not found"}, status=status.HTTP_404_NOT_FOUND)

        usuario.first_name = first_name
        usuario.last_name = last_name
        usuario.email = email
        usuario.phone_number = phone_number
        usuario.save()

        # Serialize the updated Usuario object
        serializer = UsuarioSerializer(usuario)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def carrito_productos(request):
    if request.method == 'GET':
        id_usuario = request.query_params.get('carrito')
        if not id_usuario:
            return JsonResponse({"error": "ID de usuario es requerido"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            usuario = Usuario.objects.get(id=id_usuario)
            carrito_producto = ProductoPCarrito.objects.filter(carrito=id_usuario)
        except (Carrito.DoesNotExist, Usuario.DoesNotExist):
            return JsonResponse({"error": "Usuario or Carrito not found"}, status=status.HTTP_404_NOT_FOUND)

        # Serialize the QuerySet and Usuario object
        usuario_serializer = UsuarioSerializer(usuario)
        carrito_serializer = ProductoPCarritoSerializer(carrito_producto, many=True)

        return JsonResponse({
            'usuario': usuario_serializer.data,
            'carrito_producto': carrito_serializer.data
        }, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        id_usuario = request.data.get('id_usuario')
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


@api_view(['GET', 'POST', 'DELETE'])
def carrito_pedido(request):
    if request.method == 'GET':
        id_usuario = request.data.get('userId')
        if not id_usuario:
            return JsonResponse({"error": "ID de usuario es requerido"}, status=status.HTTP_400_BAD_REQUEST)
            # Filter PedidoHistorico objects by usuario
        pedidos_historicos = PedidoHistorico.objects.filter(usuario=id_usuario)

        # Serialize the QuerySet
        serializer = PedidoHistoricoSerializer(pedidos_historicos, many=True)
        # Return the serialized data
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        user_id = request.data.get('user_id')

        if not user_id:
            return JsonResponse({"error": "ID de usuario requerido"},
                                status=status.HTTP_400_BAD_REQUEST)
        try:
            carrito = Carrito.objects.get(usuario=user_id)
        except Carrito.DoesNotExist:
            return JsonResponse({"error": "Carrito no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        nombre_empresa = request.data.get('nombre_empresa')
        rut_empresa = request.data.get('rut_empresa')
        nombre = request.data.get('nombre')
        apellido = request.data.get('apellido')
        email = request.data.get('email')
        direccion = request.data.get('direccion')
        region = request.data.get('region')
        comuna = request.data.get('comuna')
        telefono = request.data.get('telefono')
        descripcion = request.data.get('descripcion')
        metodo_pago = request.data.get('metodo_pago')
        fecha = request.data.get('fecha')

        if not nombre or not apellido or not email or not direccion or not region or not comuna or not telefono or not descripcion or not metodo_pago or not fecha:
            return JsonResponse({"error": "Todos los campos son requeridos"},
                                status=status.HTTP_400_BAD_REQUEST)
        try:
            pedido = Pedido.objects.get(carrito=carrito)
            pedido.direccion = direccion
            pedido.region = region
            pedido.comuna = comuna
            pedido.descripcion = descripcion
            pedido.fecha = fecha
            pedido.metodo_pago = metodo_pago
            pedido.nombre_empresa = nombre_empresa
            pedido.rut_empresa = rut_empresa
            pedido.phone_number = telefono
            pedido.email = email
            pedido.first_name = nombre
            pedido.last_name = apellido
            pedido.save()
            return JsonResponse({"status": "actualizado"}, status=status.HTTP_200_OK)
        except Pedido.DoesNotExist:
            pedido = Pedido.objects.create(direccion=direccion, region=region, comuna=comuna, descripcion=descripcion,
                                           fecha=fecha, metodo_pago=metodo_pago, nombre_empresa=nombre_empresa,
                                           rut_empresa=rut_empresa, carrito=carrito, phone_number=telefono, email=email,
                                           first_name=nombre, last_name=apellido)

        return JsonResponse({"status": "creado"}, status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        id_pedido = request.data.get('id_pedido')
        if not id_pedido:
            return JsonResponse({"error": "ID de usuario requerido"},
                                status=status.HTTP_400_BAD_REQUEST)
        try:
            carrito = Carrito.objects.get(usuario=id_pedido)
        except Carrito.DoesNotExist:
            return JsonResponse({"error": "Carrito no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        try:
            pedido = Pedido.objects.get(carrito=carrito)
        except Pedido.DoesNotExist:
            return JsonResponse({"error": "Pedido not found"}, status=status.HTTP_404_NOT_FOUND)

        id_pedido_historico = str(uuid.uuid4())
        # Create a PedidoHistorico instance with the same data as the Pedido instance
        pedido_creado = PedidoHistorico.objects.create(
            id_pedido=id_pedido_historico,
            usuario=pedido.carrito.usuario,
            direccion=pedido.direccion,
            region=pedido.region,
            comuna=pedido.comuna,
            descripcion=pedido.descripcion,
            fecha=pedido.fecha,
            metodo_pago=pedido.metodo_pago,
            nombre_empresa=pedido.nombre_empresa,
            rut_empresa=pedido.rut_empresa,
            first_name=pedido.first_name,
            last_name=pedido.last_name,
            email=pedido.email,
            phone_number=pedido.phone_number,
        )

        # Delete the Pedido instance
        pedido.delete()
        # ProductoPCarrito.objects.filter(carrito=carrito).delete()
        productos_pedido = ProductoPCarrito.objects.filter(carrito=carrito)

        for producto_pedido in productos_pedido:
            ProductosPedido.objects.create(
                pedido=pedido_creado,
                producto=producto_pedido.producto_carrito,
                cantidad=producto_pedido.cantidad,
                precio_total=producto_pedido.producto_carrito.precio_oferta * producto_pedido.cantidad
            )

        productos_pedido.delete()

        return JsonResponse({"id": id_pedido_historico}, status=status.HTTP_200_OK)
