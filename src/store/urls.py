from rest_framework import routers

from store.views import WarehouseViewSet, StoreOrderViewSet

router = routers.DefaultRouter()
router.register(r"warehouses", WarehouseViewSet, basename="store_warehouse")
router.register(r"order", StoreOrderViewSet, basename="store_order")

urlpatterns = []
urlpatterns += router.urls
