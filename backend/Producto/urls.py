from rest_framework import routers
from .api import ProductoViewSet

routers = routers.DefaultRouter()
routers.register('api/producto',ProductoViewSet,'producto')
urlpatterns = routers.urls