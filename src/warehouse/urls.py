from rest_framework import routers

from warehouse.views import WarehouseViewSet, WarehouseOrderViewSet

router = routers.DefaultRouter()
router.register(r"warehouses", WarehouseViewSet, basename="warehouse")
router.register(r"order", WarehouseOrderViewSet, basename="warehouse_order")

urlpatterns = []
urlpatterns += router.urls
