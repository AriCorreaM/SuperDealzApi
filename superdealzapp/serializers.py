from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class CategoriaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Categoria
		fields = ('nombre_cat')


class ProductoSerializer(serializers.ModelSerializer):
	categoria = serializers.ReadOnlyField(source='categoria.nombre_cat')

	class Meta:
		model = Producto
		fields = ('id_producto', 'marca', 'nombre', 'medida', 'imagen', 'url', 'disponible', 'categoria')
		# fields = ('__all__')


class SupermercadoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Supermercado
		fields = ('nombre_super')
		# fields = ('__all__')



class PrecioSerializer(serializers.HyperlinkedModelSerializer):
	producto = ProductoSerializer() #serializers.RelatedField(source='producto', read_only=True)
	# supermercado = SupermercadoSerializer() 
	supermercado = serializers.ReadOnlyField(source='supermercado.nombre_super')

	class Meta:
		model = Precio
		fields = ('id_precio', 'precio', 'actualizado', 'producto', 'supermercado')
		# fields = ('__all__')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')
