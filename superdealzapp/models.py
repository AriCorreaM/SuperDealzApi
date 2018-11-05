from django.db import models

class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre_cat = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'categoria'

    def __str__(self):
        return self.nombre_cat


class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    medida = models.CharField(max_length=50, blank=True, null=True)
    imagen = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255)
    disponible = models.BooleanField()
    categoria = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='id_categoria', blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'producto'

    def __str__(self):
        return self.nombre


class Error(models.Model):
    id_error = models.AutoField(primary_key=True)
    mensaje = models.TextField(blank=True, null=True)  # This field type is a guess.
    url = models.TextField(blank=True, null=True)  # This field type is a guess.
    fecha = models.DateTimeField(blank=True, null=True)
    producto = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'error'

    def __str__(self):
    	return self.url


class Supermercado(models.Model):
    id_super = models.AutoField(primary_key=True)
    nombre_super = models.CharField(max_length=100)
    main_url = models.CharField(max_length=255)
    term_use = models.CharField(max_length=255)
    logo = models.CharField(max_length=255)
    estado = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'supermercado'

    def __str__(self):
    	return self.nombre_super


class Precio(models.Model):
    id_precio = models.AutoField(primary_key=True)
    precio = models.IntegerField()
    creado = models.DateTimeField()
    actualizado = models.DateTimeField()
    producto = models.ForeignKey(Producto, models.DO_NOTHING, db_column='id_producto', blank=True, null=True)
    supermercado = models.ForeignKey(Supermercado, models.DO_NOTHING, db_column='id_super', blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'precio'

    def __str__(self):
        return self.precio