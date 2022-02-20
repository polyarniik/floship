# Create your views here.

from rest_framework import viewsets

from warehouse.models import Warehouse, WarehouseOrder
from warehouse.serializers import WarehouseSerializer, WarehouseOrderSerializer


class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.filter(is_active=True)
    serializer_class = WarehouseSerializer


class WarehouseOrderViewSet(viewsets.ModelViewSet):
    queryset = WarehouseOrder.objects.all()
    serializer_class = WarehouseOrderSerializer
