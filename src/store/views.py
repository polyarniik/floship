from rest_framework import viewsets

from store.models import StoreOrder, Warehouse
from store.serializers import StoreOrderSerializer, WarehouseSerializer


class StoreOrderViewSet(viewsets.ModelViewSet):
    queryset = StoreOrder.objects.all()
    serializer_class = StoreOrderSerializer


class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer

    def create(self, request, *args, **kwargs):
        print("here")
        print(vars(request))
        super(WarehouseViewSet, self).create(request, *args, **kwargs)
