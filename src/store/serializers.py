from rest_framework import serializers

from store.models import Warehouse, StoreOrder


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = "__all__"


class StoreOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreOrder
        fields = ("id", "number", "status", "warehouse_order_id", "warehouse")
