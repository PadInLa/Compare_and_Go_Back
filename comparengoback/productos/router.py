from rest_framework import routers

from productos.views import ProdViewSet

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'', ProdViewSet)