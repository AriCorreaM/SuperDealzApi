from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, generics, permissions # new
from .models import *
from .serializers import *

class ProductoView(viewsets.ModelViewSet):
	queryset = Producto.objects.all()
	serializer_class = ProductoSerializer


class PrecioView(viewsets.ModelViewSet):
	queryset = Precio.objects.all()
	serializer_class = PrecioSerializer


class SupermercadoView(viewsets.ModelViewSet):
	queryset = Supermercado.objects.all()
	serializer_class = SupermercadoSerializer


class CategoriaView(viewsets.ModelViewSet):
	queryset = Categoria.objects.all()
	serializer_class = CategoriaSerializer


class UserList(generics.ListAPIView): # new
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,) # new


class UserDetail(generics.RetrieveAPIView): # new
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,) # new
