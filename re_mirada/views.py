from django.core.exceptions import ValidationError
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Usuario, Carrito
from .serializers import UsuarioSerializer


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
