from django.urls import path, include
from . import views
from rest_framework import routers 
from rest_framework.schemas import get_schema_view

router = routers.DefaultRouter()
router.register('Producto', views.ProductoView)
router.register('Precio', views.PrecioView)
router.register('Supermercado', views.SupermercadoView)
router.register('Categoria', views.CategoriaView)



schema_view = get_schema_view(title='Pastebin API')

urlpatterns = [
	path('', include(router.urls)),
	path('users/', views.UserList.as_view()), # new
    path('users/<int:pk>/', views.UserDetail.as_view()), # new
    path('schema/', schema_view),
]